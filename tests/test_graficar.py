import tempfile
import unittest
from pathlib import Path
from PIL import Image
from scripts.graficar import crear_grafico, resumen_grafico

class GraficoTest(unittest.TestCase):
    def test_png_desde_datos_propios(self):
        with tempfile.TemporaryDirectory() as temp:
            csv, png = Path(temp)/'datos.csv', Path(temp)/'grafico.png'
            csv.write_text('lugar,valor\nA,24\nB,30\n', encoding='utf-8')
            summary = crear_grafico(csv, png)
            self.assertEqual(summary['promedio'], 27)
            self.assertGreater(png.stat().st_size, 1000)
            with Image.open(png) as image:
                self.assertEqual(image.format, 'PNG')
                self.assertEqual(image.size, (1620, 900))

    def test_resumen_lee_tamano_real_tras_cambiar_figsize_y_dpi(self):
        with tempfile.TemporaryDirectory() as temp:
            csv, png = Path(temp)/'datos.csv', Path(temp)/'grafico.png'
            csv.write_text('lugar,valor\nA,2\nB,4\n', encoding='utf-8')
            summary = crear_grafico(csv, png, figsize=(7, 4), dpi=100)
            markdown = resumen_grafico(summary, png)
            self.assertIn('700 × 400', markdown)
            self.assertNotIn('1620 × 900', markdown)

if __name__ == '__main__':
    unittest.main()
