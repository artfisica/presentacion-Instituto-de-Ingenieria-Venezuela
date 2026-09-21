# Parche previo al push: fuentes y dimensiones

Este parche se aplica sobre el ZIP anterior de la primera tanda de feedback.
Incluye fuentes reducidas, validación por fuente efectiva, dimensiones reales del
PNG, pruebas y el PDF de referencia regenerado. También se entrega un ZIP completo
con el mismo estado final: **elige una de las dos entregas**.

## Usar el parche pequeño

Guarda el archivo con el nombre exacto `parche-fuentes-y-dimensiones.zip` en
Descargas. Si el navegador añade `__1_`, `(1)` u otro sufijo, renómbralo primero.

```bash
cd ~/Downloads
unzip parche-fuentes-y-dimensiones.zip -d charla-parche
cd ~/Downloads/charla-instituto/presentacion-Instituto-de-Ingenieria-Venezuela
ditto ~/Downloads/charla-parche/presentacion-Instituto-de-Ingenieria-Venezuela .
```

Si tu clon está en otra carpeta, cambia ese `cd`. Revisa antes cualquier edición
propia que pudiera coincidir con los archivos del parche.

## Retirar exactamente las tres fuentes obsoletas

`ditto` mezcla carpetas; no elimina los archivos retirados. Desde la raíz del clon,
ejecuta estas tres eliminaciones específicas, tanto si copiaste el parche como si
copiaste el ZIP completo sobre la entrega anterior:

```bash
rm -f -- fuentes/DejaVuSansMono-Bold.ttf
rm -f -- fuentes/DejaVuSansMono-Oblique.ttf
rm -f -- fuentes/DejaVuSansMono-BoldOblique.ttf
```

El paquete final debe tener **cinco TTF**. No borres la variante Sans-BoldOblique:
conserva la cursiva de los títulos en negrita. La prueba de tamaño detectará si
queda alguna variante antigua.

## Comprobar y subir tú los cambios

Con el entorno Python del proyecto activado:

```bash
python -m unittest discover -s tests -v
python scripts/crear_pdf.py
python scripts/graficar.py
python web/build.py
python web/validate.py
git status --short
git add -A
git diff --cached --stat
git commit -m "Reduce PDF fonts and validate glyphs per rendered face"
git push
```

Las dependencias de ejecución no cambian. `git add -A` incluye las eliminaciones
si las fuentes anteriores ya estaban preparadas o versionadas. Este parche no
reescribe historial, no crea etiquetas y no modifica GitHub por sí mismo.

La prueba del gráfico cambia `figsize` y `dpi` y verifica que el resumen utiliza
las dimensiones del PNG guardado. Las pruebas del PDF comprueban tanto símbolos
científicos como un carácter permitido en Sans pero ausente en Mono, indicando la
línea real incluso dentro de un párrafo de varias líneas.

La tarjeta social, JSON-LD, devcontainer, comprobación del entorno y publicación
propia siguen en la siguiente tanda. `CITATION.cff` permanece sin DOI, versión o
fecha de release hasta que tú prepares y publiques esa versión.
