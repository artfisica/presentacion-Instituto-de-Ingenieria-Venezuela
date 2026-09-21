import tempfile
import unittest
from pathlib import Path
from PIL import Image
from scripts.crear_pdf import crear_pdf, ROOT

class PdfTest(unittest.TestCase):
    def test_cambios_de_texto_e_imagen_regeneran_pdf(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            folder = Path(temp)
            image, source, pdf = folder/'foto.jpg', folder/'informe.md', folder/'informe.pdf'
            Image.new('RGB', (80, 40), 'blue').save(image)
            source.write_text('# Informe\n\nTexto inicial.\n\n![Ejemplo](foto.jpg)\n', encoding='utf-8')
            crear_pdf(source, pdf)
            original = pdf.read_bytes()
            self.assertTrue(original.startswith(b'%PDF-'))
            crear_pdf(source, pdf)
            self.assertEqual(original, pdf.read_bytes())
            source.write_text(source.read_text().replace('inicial', 'actualizado'), encoding='utf-8')
            crear_pdf(source, pdf)
            changed_text = pdf.read_bytes()
            self.assertNotEqual(original, changed_text)
            Image.new('RGB', (80, 40), 'red').save(image)
            crear_pdf(source, pdf)
            self.assertNotEqual(changed_text, pdf.read_bytes())

    def test_imagen_ausente_produce_error_claro(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp:
            source = Path(temp)/'informe.md'
            source.write_text('![Foto](no-existe.jpg)', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Imagen local inexistente'):
                crear_pdf(source, Path(temp)/'salida.pdf')

if __name__ == '__main__':
    unittest.main()
