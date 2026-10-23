# Salidas de referencia

Estas salidas se generaron con los archivos originales de este paquete:

- `grafico.png`: gráfico del CSV de ejemplo.
- `informe.pdf`: documento de `ejemplos/informe.md`, con fuentes DejaVu incrustadas.
- `informe-vista-previa.png`: primera página del PDF, para leer desde GitHub.
- `resumen.json`: seis valores, promedio 25, mínimo 23, máximo 27 y hash del CSV.

Son ejemplos estáticos que se conservan en Git. Los ejercicios escriben en
`resultados/`; no sustituyen estas referencias cuando cambias los datos. El
informe incluye una fotografía ATLAS/CERN: se conserva su crédito y la excepción
de licencia descrita en `../../THIRD_PARTY.md`.

Para regenerar las salidas después de una modificación intencionada del ejemplo:

```bash
python scripts/analizar.py
python scripts/graficar.py
python scripts/crear_pdf.py
cp resultados/grafico.png resultados/informe.pdf resultados/resumen.json ejemplos/salida-esperada/
```

Si cambias el PDF, actualiza también su miniatura y la vista previa de la web.
Con Poppler instalado (`pdftoppm`) y el entorno Python activado:

```bash
pdftoppm -f 1 -singlefile -scale-to 1200 -png ejemplos/salida-esperada/informe.pdf resultados/informe-vista-previa
cp resultados/informe-vista-previa.png ejemplos/salida-esperada/informe-vista-previa.png
python -c "from PIL import Image; im = Image.open('resultados/informe-vista-previa.png'); im.thumbnail((600, 849)); im.save('web/assets/ejemplo-pdf.webp', quality=80)"
python web/validate.py
```

Poppler solo se utiliza para mantener estas imágenes estáticas; los ejercicios
y la web no lo necesitan. La referencia actual contiene dos páginas; las
miniaturas muestran únicamente la primera. La procedencia de la fotografía
del Instituto está pendiente de documentar en `../../imagenes/README.md`.
