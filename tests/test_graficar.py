import tempfile
import unittest
from unittest.mock import patch
from matplotlib.figure import Figure
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

    def test_lugares_repetidos_conservan_todas_las_barras(self):
        with tempfile.TemporaryDirectory() as temp:
            csv, png = Path(temp)/'datos.csv', Path(temp)/'grafico.png'
            csv.write_text('lugar,valor\nA,24\nA,30\nB,25\n', encoding='utf-8')
            savefig = Figure.savefig
            captured = {}
            def inspect(fig, *args, **kwargs):
                ax = fig.axes[0]
                captured['centres'] = [bar.get_y() + bar.get_height()/2 for bar in ax.patches]
                captured['labels'] = [label.get_text() for label in ax.get_yticklabels()]
                return savefig(fig, *args, **kwargs)
            with patch.object(Figure, 'savefig', inspect):
                summary = crear_grafico(csv, png)
            self.assertEqual(len(set(captured['centres'])), 3)
            self.assertEqual(captured['labels'], ['A', 'A', 'B'])
            self.assertEqual(summary['n'], 3)
            self.assertEqual(summary['promedio'], 79/3)

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
