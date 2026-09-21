# Fuentes del PDF: cinco variantes, 536.336 bytes

Las fuentes son subconjuntos de DejaVu: conservan los glifos utilizados por este
material y un repertorio científico explícito. El paquete anterior incluía ocho
TTF (3.912.124 bytes); este contiene cinco (536.336 bytes), un 86,3 % menos.
No se descargan fuentes ni se necesita fontTools para ejecutar el PDF.

| Variante | Bytes | Uso |
|---|---:|---|
| DejaVuSans | 120.032 | Texto y pies de página. |
| DejaVuSans-Bold | 112.584 | Títulos y negritas. |
| DejaVuSans-Oblique | 113.024 | Cursivas. |
| DejaVuSans-BoldOblique | 116.160 | Cursivas en títulos y estilos combinados. |
| DejaVuSansMono | 74.536 | Código entre comillas invertidas, siempre en variante normal. |

La quinta variante evita perder la cursiva de un título que ya se dibuja en
negrita. Se han retirado las tres variantes Mono en negrita y/o cursiva.

## Repertorio y validación

El subconjunto conserva, donde la fuente original los incluía, latín y Latin
Extended-A, diacríticos combinantes, griego, puntuación general, superíndices y
subíndices, símbolos monetarios, símbolos como ℃, flechas, operadores matemáticos,
★ y ☑. Los rangos exactos están en `subsets.json`.

Cada fragmento se valida contra **la fuente que ReportLab usará para dibujarlo**,
después de resolver negrita, cursiva y código. No se utiliza una intersección
global de glifos. Por ejemplo, ℃ funciona en texto Sans, pero produce un error
explícito si se escribe en un fragmento Mono, que no dispone de ese glifo.

Los destinos de enlaces y las rutas de archivos no se validan como texto visible.
Un glifo ausente en texto impreso produce un error con el carácter, código Unicode,
fuente y línea del Markdown. Las líneas de un párrafo se siguen uniendo normalmente
en el PDF, aunque se conservan por separado para identificar errores.

## Reproducir la reducción (solo mantenimiento)

Fuente de partida: los TTF DejaVu incluidos en Matplotlib 3.10.8. Herramienta:
fontTools 4.61.1. Se mantiene `LICENSE_DEJAVU`; no se modificaron diseños de glifos.
`subsets.json` registra el SHA-256 de cada original y cada archivo resultante.

En un entorno de mantenimiento con esas dos versiones instaladas:

```bash
font_source="$(python -c 'import matplotlib; print(matplotlib.get_data_path())')/fonts/ttf"
for face in DejaVuSans DejaVuSans-Bold DejaVuSans-Oblique DejaVuSans-BoldOblique DejaVuSansMono
do
  python -m fontTools.subset "$font_source/$face.ttf" \
    --output-file="fuentes/$face.ttf" \
    --unicodes='U+0020-017F,U+0300-03FF,U+2000-214F,U+2190-22FF,U+2605,U+2611' \
    --no-hinting --name-IDs+=13,14 --drop-tables+=FFTM --no-recalc-timestamp
done
```

Los estudiantes no necesitan ejecutar estos comandos. Para ampliar el repertorio,
parte de los originales, amplía los rangos y actualiza las pruebas y el manifiesto.
La referencia de las opciones es la [documentación de fontTools](https://fonttools.readthedocs.io/en/latest/subset/index.html).
