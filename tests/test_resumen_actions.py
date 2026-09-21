import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from scripts.resumen_actions import escribir_resumen, tabla_numeros

class ResumenTest(unittest.TestCase):
    def test_resumen_se_anade_sin_borrar_otros_pasos(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)/'summary.md'
            path.write_text('Paso anterior\n', encoding='utf-8')
            with patch.dict(os.environ, {'GITHUB_STEP_SUMMARY': str(path)}):
                escribir_resumen(tabla_numeros({'n': 6, 'promedio': 25, 'minimo': 23, 'maximo': 27}))
            text = path.read_text()
            self.assertTrue(text.startswith('Paso anterior'))
            self.assertIn('| 6 | 25 | 23 | 27 |', text)

    def test_ejecucion_local_sin_variable(self):
        with patch.dict(os.environ, {}, clear=True):
            escribir_resumen('Sin conexión ni archivo que crear.')
