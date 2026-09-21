#!/usr/bin/env python3
"""Create a PNG chart from the same CSV used in the first exercise."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from analizar import leer_datos

ROOT = Path(__file__).resolve().parents[1]

def main():
    datos = leer_datos(ROOT/'datos/mediciones.csv')
    nombres = [fila['lugar'] for fila in datos]
    valores = [fila['valor'] for fila in datos]
    fig, ax = plt.subplots(figsize=(9, 5), layout='constrained')
    barras = ax.barh(nombres, valores, color='#144de8')
    ax.bar_label(barras, padding=5, fmt='%g')
    ax.invert_yaxis()
    ax.set_title('Comparar para comprender', loc='left', fontsize=20, pad=22)
    ax.set_xlabel('Valor de ejemplo (datos ficticios, sin unidades asignadas)')
    ax.spines[['top', 'right']].set_visible(False)
    ax.margins(x=0.15)
    destino = ROOT/'resultados'
    destino.mkdir(exist_ok=True)
    fig.savefig(destino/'grafico.png', dpi=180)
    plt.close(fig)
    print(f'Gráfico generado: {destino / "grafico.png"}')

if __name__ == '__main__':
    main()
