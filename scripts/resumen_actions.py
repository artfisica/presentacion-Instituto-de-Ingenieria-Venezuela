"""Optional run-page feedback. Local execution requires no GitHub connection."""
import os
from pathlib import Path

def escribir_resumen(markdown):
    destino = os.environ.get('GITHUB_STEP_SUMMARY')
    if destino:
        with Path(destino).open('a', encoding='utf-8') as stream:
            stream.write(markdown.rstrip() + '\n\n')

def tabla_numeros(resumen):
    return ('| Datos | Promedio | Mínimo | Máximo |\n'
            '|---:|---:|---:|---:|\n'
            f"| {resumen['n']} | {resumen['promedio']:g} | {resumen['minimo']:g} | {resumen['maximo']:g} |")
