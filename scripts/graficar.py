#!/usr/bin/env python3
"""Create a PNG chart from the same CSV used in the first exercise."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import sys
if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.resumen_actions import escribir_resumen, tabla_numeros
from scripts.analizar import leer_datos, resumir

ROOT = Path(__file__).resolve().parents[1]

def crear_grafico(entrada=ROOT/'datos/mediciones.csv', salida=ROOT/'resultados/grafico.png', *, figsize=(9, 5), dpi=180):
    datos = leer_datos(entrada)
    nombres = [fila['lugar'] for fila in datos]
    valores = [fila['valor'] for fila in datos]
    fig, ax = plt.subplots(figsize=figsize, layout='constrained')
    barras = ax.barh(nombres, valores, color='#144de8')
    ax.bar_label(barras, padding=5, fmt='%g')
    ax.invert_yaxis()
    ax.set_title('Comparar para comprender', loc='left', fontsize=20, pad=22)
    ax.set_xlabel('Valor de ejemplo (datos ficticios, sin unidades asignadas)')
    ax.spines[['top', 'right']].set_visible(False)
    ax.margins(x=0.15)
    salida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(salida, dpi=dpi)
    plt.close(fig)
    print(f'Gráfico generado: {salida}')
    return resumir(datos)

def resumen_grafico(summary, salida):
    with Image.open(salida) as image:
        ancho, alto = image.size
    return ('## 02 · Gráfico listo\n\n'+tabla_numeros(summary)+
            f'\n\nPNG de {ancho} × {alto} píxeles disponible en el artefacto **grafico**.')

if __name__ == '__main__':
    salida = ROOT/'resultados/grafico.png'
    summary = crear_grafico(salida=salida)
    escribir_resumen(resumen_grafico(summary, salida))
