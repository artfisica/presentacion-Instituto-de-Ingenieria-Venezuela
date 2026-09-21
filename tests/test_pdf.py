import tempfile
import unittest
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
from scripts.crear_pdf import crear_pdf, ROOT

class PdfTest(unittest.TestCase):
    def setUp(self):
        (ROOT/'.tmp').mkdir(exist_ok=True)

    def test_simbolos_cientificos_y_estilos(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as temp:
            source, pdf = Path(temp)/'simbolos.md', Path(temp)/'simbolos.pdf'
            sample = 'Propuesta → simulación · CO₂ · μ⁺μ⁻ · σ = 1,2×10⁻³ · Δm² · α β γ Ω · ≤ ± µ ° «ñ» …'
            source.write_text('# '+sample+'\n\n'+sample+'\n\n**'+sample+'**\n\n*'+sample+'*\n\n`'+sample+'`', encoding='utf-8')
            pages = crear_pdf(source, pdf)
            reader = PdfReader(pdf)
            self.assertEqual(pages, len(reader.pages))
            text = '\n'.join(page.extract_text() for page in reader.pages)
            self.assertEqual(' '.join(text.split()).count(sample), 5)

    def test_validacion_segun_fuente_y_linea_real(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as temp:
            source, pdf = Path(temp)/'fuentes.md', Path(temp)/'fuentes.pdf'
            source.write_text('# *Título inclinado*\n\nTemperatura ℃, estrella ★ y casilla ☑.\n', encoding='utf-8')
            crear_pdf(source, pdf)
            text = ' '.join(page.extract_text() for page in PdfReader(pdf).pages)
            self.assertIn('℃', text)
            self.assertIn('★', text)
            self.assertIn('☑', text)
            # Same symbol is allowed in Sans on line 2, but missing in Mono
            # on line 3 of the same paragraph; retain the actual source line.
            source.write_text('# Informe\nTemperatura ℃ en texto.\nTemperatura `℃` en código.\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, r'línea 3:.*U\+2103.*DejaVuSansMono'):
                crear_pdf(source, pdf)

    def test_no_valida_glifos_en_destinos_no_impresos(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as temp:
            source, pdf = Path(temp)/'enlace.md', Path(temp)/'enlace.pdf'
            source.write_text('[Fuente](https://example.org/漢)', encoding='utf-8')
            crear_pdf(source, pdf)
            self.assertIn('Fuente', PdfReader(pdf).pages[0].extract_text())

    def test_paquete_de_fuentes_compacto(self):
        fonts = list((ROOT/'fuentes').glob('*.ttf'))
        self.assertEqual(len(fonts), 5)
        self.assertLess(sum(p.stat().st_size for p in fonts), 600_000)

    def test_caracter_sin_glifo_falla_explicitamente(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as temp:
            source = Path(temp)/'simbolos.md'
            source.write_text('Texto \U0001F9EC', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, r'U\+1F9EC'):
                crear_pdf(source, Path(temp)/'salida.pdf')

    def test_cambios_de_texto_e_imagen_regeneran_pdf(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as temp:
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

    def test_mismo_contenido_en_otra_carpeta_produce_el_mismo_pdf(self):
        # Dos copias del repositorio, en rutas distintas, deben generar bytes
        # idénticos: la reproducibilidad no puede depender de dónde se trabaje.
        salidas = []
        for nombre in ('copia-uno', 'copia-dos'):
            with tempfile.TemporaryDirectory(dir=ROOT/'.tmp', prefix=nombre) as temp:
                carpeta = Path(temp)
                imagen, source, pdf = carpeta/'foto.jpg', carpeta/'informe.md', carpeta/'informe.pdf'
                Image.new('RGB', (80, 40), 'blue').save(imagen)
                source.write_text('# Informe\n\nTexto.\n\n![Ejemplo](foto.jpg)\n', encoding='utf-8')
                crear_pdf(source, pdf)
                salidas.append(pdf.read_bytes())
        self.assertEqual(*salidas)

    def test_imagen_ausente_produce_error_claro(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.tmp') as temp:
            source = Path(temp)/'informe.md'
            source.write_text('![Foto](no-existe.jpg)', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Imagen local inexistente'):
                crear_pdf(source, Path(temp)/'salida.pdf')

if __name__ == '__main__':
    unittest.main()
