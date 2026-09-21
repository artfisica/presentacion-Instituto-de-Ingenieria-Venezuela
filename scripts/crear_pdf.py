#!/usr/bin/env python3
"""Small Markdown teaching renderer: headings, paragraphs, lists and images.

Supports #/##/###, **bold**, *italic*, `code`, links, and one image per line.
It intentionally does not implement tables, raw HTML or fenced code blocks.
"""
import argparse
from html import escape
from io import BytesIO
from pathlib import Path
import re
import unicodedata
import sys
if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.resumen_actions import escribir_resumen


from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, KeepTogether

ROOT = Path(__file__).resolve().parents[1]

def registrar_fuentes():
    # Four proportional faces preserve italic headings and combined styles.
    names = ['DejaVuSans'+suffix for suffix in ('', '-Bold', '-Oblique', '-BoldOblique')]
    names.append('DejaVuSansMono')
    for name in names:
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(ROOT/'fuentes'/f'{name}.ttf')))
    pdfmetrics.registerFontFamily('DejaVuSans', normal='DejaVuSans', bold='DejaVuSans-Bold',
                                 italic='DejaVuSans-Oblique', boldItalic='DejaVuSans-BoldOblique')
    # Backtick code spans always use the one regular monospace face.
    pdfmetrics.registerFontFamily('DejaVuSansMono', normal='DejaVuSansMono', bold='DejaVuSansMono',
                                 italic='DejaVuSansMono', boldItalic='DejaVuSansMono')

def validar_caracteres(texto, fuente, linea=1):
    disponibles = pdfmetrics.getFont(fuente).face.charToGlyph
    for offset, line in enumerate(texto.splitlines()):
        for char in line:
            if char != '\t' and not disponibles.get(ord(char)):
                nombre = unicodedata.name(char, 'SIN NOMBRE')
                raise ValueError(f'Carácter no compatible en línea {linea+offset}: {char!r} '
                                 f'(U+{ord(char):04X}, {nombre}), fuente {fuente}. '
                                 'Usa una notación equivalente o amplía esa fuente.')

def parrafo_validado(texto, estilo, linea, **kwargs):
    markup = formato(texto)
    # A validation-only paragraph preserves source line boundaries. ReportLab
    # resolves the exact font of each fragment, including bold/italic/code.
    preview = Paragraph(markup.replace('\n', '<br/>'), estilo, **kwargs)
    current_line = linea
    for fragment in preview.frags:
        if getattr(fragment, 'lineBreak', False):
            current_line += 1
        else:
            validar_caracteres(getattr(fragment, 'text', ''), fragment.fontName, current_line)
    # Markdown paragraph lines still flow together in the final document.
    return Paragraph(markup.replace('\n', ' '), estilo, **kwargs)


def formato(text):
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<link href="\2" color="#144de8">\1</link>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return re.sub(r'`([^`]+)`', r'<font name="DejaVuSansMono">\1</font>', text)

def crear_pdf(entrada, salida):
    entrada = entrada.resolve()
    texto = entrada.read_text(encoding='utf-8')
    registrar_fuentes()
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'DejaVuSans'
    styles['Normal'].fontSize = 11
    styles['Normal'].leading = 16
    styles['Normal'].spaceAfter = 10
    styles['Normal'].textColor = colors.HexColor('#102434')
    for name, size in [('Heading1', 27), ('Heading2', 17), ('Heading3', 13)]:
        styles[name].fontName = 'DejaVuSans-Bold'
        styles[name].fontSize = size
        styles[name].leading = size * 1.2
        styles[name].textColor = colors.HexColor('#144de8')
        styles[name].spaceBefore = 12
        styles[name].spaceAfter = 10
    styles.add(ParagraphStyle('CaptionSmall', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#536674')))
    story, pending = [], []

    def flush():
        if pending:
            story.append(parrafo_validado('\n'.join(text for _, text in pending), styles['Normal'], pending[0][0]))
            pending.clear()

    for numero, line in enumerate(texto.splitlines(), 1):
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
            datos = path.read_bytes()
            width, height = ImageReader(BytesIO(datos)).getSize()
            scale = min(1, 475/width, 235/height)
            # Los bytes, y no la ruta del ordenador, identifican la imagen dentro
            # del PDF: dos copias del repositorio producen el mismo documento.
            imagen = Image(BytesIO(datos), width*scale, height*scale)
            story.append(KeepTogether([imagen, Spacer(1, 7), parrafo_validado(caption, styles['CaptionSmall'], numero)]))
        elif match_heading:
            flush()
            story.append(parrafo_validado(match_heading[2], styles[f'Heading{len(match_heading[1])}'], numero))
        elif line.startswith('- '):
            flush()
            story.append(parrafo_validado(line[2:], styles['Normal'], numero, bulletText='-'))
        elif line.startswith(('```', '|', '<')):
            raise ValueError('Este ejemplo admite Markdown sencillo, sin tablas, HTML ni bloques de código.')
        else:
            pending.append((numero, line))
    flush()
    if not story:
        raise ValueError('El documento Markdown está vacío.')
    salida.parent.mkdir(parents=True, exist_ok=True)
    def pie(canvas, doc):
        canvas.setFont('DejaVuSans', 8)
        canvas.setFillColor(colors.HexColor('#536674'))
        canvas.drawString(60, 30, 'Del texto al documento | Instituto de Ingeniería, Venezuela')
        canvas.drawRightString(A4[0]-60, 30, str(doc.page))
    documento = SimpleDocTemplate(str(salida), pagesize=A4, rightMargin=60, leftMargin=60,
                      topMargin=40, bottomMargin=50, title='Mi primer informe reproducible',
                      author='Participante', invariant=1)
    documento.build(story, onFirstPage=pie, onLaterPages=pie)
    print(f'PDF generado: {salida}')
    return documento.page

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entrada', type=Path, default=ROOT/'ejemplos/informe.md')
    parser.add_argument('--salida', type=Path, default=ROOT/'resultados/informe.pdf')
    args = parser.parse_args()
    try:
        pages = crear_pdf(args.entrada, args.salida)
        escribir_resumen(f'## 03 · Tu PDF está listo\n\n**{pages} página(s)** generada(s) desde Markdown e imágenes. Descarga el artefacto **documento-pdf**.\n\nFuente Unicode incluida; los caracteres sin glifo producen un error explícito.')
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
