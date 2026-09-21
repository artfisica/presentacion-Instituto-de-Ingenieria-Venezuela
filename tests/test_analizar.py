import tempfile
import unittest
from pathlib import Path
from scripts.analizar import ejecutar, leer_datos, resumir, ROOT

class AnalisisTest(unittest.TestCase):
    def test_ejemplo_conocido(self):
        self.assertEqual(resumir([{'lugar': str(i), 'valor': value} for i, value in enumerate([24, 26, 25, 23, 27, 25])]),
                         {'n': 6, 'promedio': 25.0, 'minimo': 23.0, 'maximo': 27.0})

    def test_rechaza_datos_invalidos(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'datos.csv'
            for content in ['lugar,valor\n', 'nombre,valor\nA,1\n', 'lugar,valor\nA,NaN\n', 'lugar,valor\nA,texto\n']:
                p.write_text(content)
                with self.assertRaises(ValueError):
                    leer_datos(p)

    def test_informe_escapa_etiquetas_y_es_reproducible(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'datos.csv'
            p.write_text('lugar,valor\n<script>,2\nB,-4\n', encoding='utf-8')
            for dest in ('uno', 'dos'):
                ejecutar(p, Path(d)/dest)
            for file in ('informe.html', 'resumen.json'):
                self.assertEqual((Path(d)/'uno'/file).read_bytes(), (Path(d)/'dos'/file).read_bytes())
            report = (Path(d)/'uno/informe.html').read_text()
            self.assertIn('&lt;script&gt;', report)
            self.assertNotIn('<script>', report)

if __name__ == '__main__':
    unittest.main()
