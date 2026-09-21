#!/usr/bin/env python3
"""CSV -> summary + HTML. Python standard library; fictional teaching data."""
import argparse
import csv
import hashlib
import json
import math
from html import escape
from pathlib import Path
from statistics import mean
import sys
if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.resumen_actions import escribir_resumen, tabla_numeros


ROOT = Path(__file__).resolve().parents[1]

def leer_datos(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if not {'lugar', 'valor'} <= set(reader.fieldnames or []):
            raise ValueError('El CSV necesita columnas lugar,valor / Required columns: lugar,valor')
        rows = []
        for line, row in enumerate(reader, 2):
            label = (row.get('lugar') or '').strip()
            try:
                value = float(row.get('valor', ''))
            except (ValueError, TypeError):
                raise ValueError(f'Fila / Row {line}: valor no numerico / non-numeric value') from None
            if not label or not math.isfinite(value):
                raise ValueError(f'Fila / Row {line}: nombre vacio o valor no finito / empty name or non-finite value')
            rows.append({'lugar': label, 'valor': value})
    if not rows:
        raise ValueError('El CSV no contiene datos / CSV contains no data')
    return rows

def resumir(rows):
    values = [row['valor'] for row in rows]
    return {'n': len(values), 'promedio': mean(values), 'minimo': min(values), 'maximo': max(values)}

def ejecutar(input_path, output_path):
    rows = leer_datos(input_path)
    summary = resumir(rows)
    digest = hashlib.sha256(input_path.read_bytes()).hexdigest()
    output_path.mkdir(parents=True, exist_ok=True)
    result = {'archivo': input_path.name, 'sha256': digest, **summary}
    (output_path/'resumen.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    table = ''.join(f'<tr><td>{escape(r["lugar"])}</td><td>{r["valor"]:g}</td></tr>' for r in rows)
    report = f'''<!doctype html><html lang="es"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Mi primer informe / My first report</title>
<style>body{{max-width:800px;margin:50px auto;padding:0 24px;font:18px/1.6 system-ui;color:#102434}}h1{{line-height:1.1}}table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;border-bottom:1px solid #ddd;padding:12px}}code{{overflow-wrap:anywhere}}.result{{background:#ddf58f;padding:20px}}</style>
<h1>Mi primer informe<br><small>My first report</small></h1>
<p>Ejemplo educativo / Teaching example. Los datos incluidos son ficticios; al adaptar el proyecto, documenta tus fuentes y unidades en ejercicios/NOTAS.md.</p>
<p class="result">N = {summary['n']} · Promedio / Mean = {summary['promedio']:g}<br>Min = {summary['minimo']:g} · Max = {summary['maximo']:g}</p>
<table><thead><tr><th>Lugar / Place</th><th>Valor / Value</th></tr></thead><tbody>{table}</tbody></table>
<p>Archivo / File: {escape(input_path.name)}<br>SHA-256: <code>{digest}</code></p>
<p>El hash permite identificar los datos usados. No certifica su veracidad. / The hash identifies the input; it does not certify its truth.</p></html>'''
    (output_path/'informe.html').write_text(report, encoding='utf-8')
    return summary

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entrada', type=Path, default=ROOT/'datos/mediciones.csv')
    parser.add_argument('--salida', type=Path, default=ROOT/'resultados')
    args = parser.parse_args()
    try:
        summary = ejecutar(args.entrada, args.salida)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
    escribir_resumen('## 01 · Análisis listo\n\n'+tabla_numeros(summary)+'\n\nEl informe HTML y el JSON están en el artefacto **analisis**.')
    print(json.dumps(summary, ensure_ascii=False))
    print(f'Informe / Report: {args.salida / "informe.html"}')
