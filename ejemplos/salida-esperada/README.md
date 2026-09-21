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

Si cambias el PDF, actualiza también su miniatura y las vistas previas de la web.
