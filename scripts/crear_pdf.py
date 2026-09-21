#!/usr/bin/env python3
"""Small Markdown teaching renderer: headings, paragraphs, lists and images.

Supports #/##/###, **bold**, *italic*, `code`, links, and one image per line.
It intentionally does not implement tables, raw HTML or fenced code blocks.
"""
import argparse
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, KeepTogether

ROOT = Path(__file__).resolve().parents[1]

def formato(text):
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<link href="\2" color="#144de8">\1</link>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', text)

def crear_pdf(entrada, salida):
    entrada = entrada.resolve()
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'Helvetica'
    styles['Normal'].fontSize = 11
    styles['Normal'].leading = 16
    styles['Normal'].spaceAfter = 10
    styles['Normal'].textColor = colors.HexColor('#102434')
    for name, size in [('Heading1', 27), ('Heading2', 17), ('Heading3', 13)]:
        styles[name].fontSize = size
        styles[name].leading = size * 1.2
        styles[name].textColor = colors.HexColor('#144de8')
        styles[name].spaceBefore = 12
        styles[name].spaceAfter = 10
    styles.add(ParagraphStyle('CaptionSmall', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#536674')))
    story, pending = [], []

    def flush():
        if pending:
            story.append(Paragraph(formato(' '.join(pending)), styles['Normal']))
            pending.clear()

    for line in entrada.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            flush()
            continue
        match_image = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        match_heading = re.match(r'^(#{1,3})\s+(.+)$', line)
        if match_image:
            flush()
            caption, relative = match_image.groups()
            path = (entrada.parent/relative).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                raise ValueError(f'Imagen local inexistente o fuera del proyecto: {relative}')
            width, height = ImageReader(str(path)).getSize()
            scale = min(475/width, 235/height)
            story.append(KeepTogether([Image(str(path), width*scale, height*scale), Spacer(1, 7), Paragraph(formato(caption), styles['CaptionSmall'])]))
        elif match_heading:
            flush()
            story.append(Paragraph(formato(match_heading[2]), styles[f'Heading{len(match_heading[1])}']))
        elif line.startswith('- '):
            flush()
            story.append(Paragraph(formato(line[2:]), styles['Normal'], bulletText='-'))
        elif line.startswith(('```', '|', '<')):
            raise ValueError('Este ejemplo admite Markdown sencillo, sin tablas, HTML ni bloques de código.')
        else:
            pending.append(line)
    flush()
    if not story:
        raise ValueError('El documento Markdown está vacío.')
    salida.parent.mkdir(parents=True, exist_ok=True)
    def pie(canvas, doc):
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#536674'))
        canvas.drawString(60, 30, 'Del texto al documento | Instituto de Ingeniería, Venezuela')
        canvas.drawRightString(A4[0]-60, 30, str(doc.page))
    SimpleDocTemplate(str(salida), pagesize=A4, rightMargin=60, leftMargin=60,
                      topMargin=40, bottomMargin=50, title='Mi primer informe reproducible',
                      author='Participante', invariant=1).build(story, onFirstPage=pie, onLaterPages=pie)
    print(f'PDF generado: {salida}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entrada', type=Path, default=ROOT/'ejemplos/informe.md')
    parser.add_argument('--salida', type=Path, default=ROOT/'resultados/informe.pdf')
    args = parser.parse_args()
    try:
        crear_pdf(args.entrada, args.salida)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
