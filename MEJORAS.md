# Estado del feedback

## Primera tanda aplicada

- Licencias MIT y CC BY 4.0 con alcance por componente y excepciones de terceros.
- CITATION.cff, guía para Zenodo y release v1.0 sin inventar DOI ni fecha.
- DejaVu TTF para PDF, familias normal/negrita/cursiva/monoespaciada y error con
  carácter, código Unicode y línea cuando falte un glifo.
- Pruebas que extraen texto del PDF y comprueban flechas, subíndices y griego.
- Resúmenes de Actions con números, páginas y enlace al resultado descargable.
- Salidas de referencia en Git, imágenes en README y vistas previas en la web.
- Quickstart al principio y badges de los cuatro flujos y las licencias.
- Navegación horizontal móvil, modo oscuro, enlace de marca funcional y aviso
  visible de fecha/enlace pendientes.
- Temporales de PDF en `.tmp/`, dependencias directas Pillow/pypdf declaradas,
  prueba del gráfico, ejecución de scripts tanto directa como con `python -m`,
  y límite de ampliación de imágenes pequeñas.
- Presupuesto de recursos de la web de 600.000 bytes en `web/validate.py`.

## Configuración que realiza Arturo

- Aplicar esta actualización y comprobar las ejecuciones en GitHub.
- Activar Template repository; establecer descripción, homepage y topics.
- Conectar Zenodo, completar la fecha/versión real y publicar la release v1.0.
- Añadir al repositorio el DOI que Zenodo asigne.

Pasos exactos en `ACTUALIZAR.md`. El asistente no realiza estas operaciones.

## Siguientes tandas, aún no implementadas

- Tarjeta social JPG 1200×630, Twitter card y Person JSON-LD.
- Fecha/enlace reales y calendario ICS cuando los confirme la organización.
- Devcontainer Python 3.12, notebook y comprobación del entorno en un comando.
- Cuarto ejercicio de publicación propia y URL base derivada de la copia.
- Galería de participantes, validación de aportes y ciclo completo de PR.
- Discussions, plantilla de preguntas y CONTRIBUTING.md.
- Comprobación de deriva de HTML generado; debe coordinarse con las URLs de
  copias para evitar que una diferencia de entorno cause falsos fallos.
- Dependabot y revisión periódica de enlaces con creación de issues.
- Considerar otro nombre después de la charla; comprobar los efectos sobre
  GitHub Pages y enlaces antes de decidir una migración.

El diagrama mínimo de cuatro pasos se mantiene por ahora como explicación en
texto: editar, guardar un commit, ejecutar la acción y revisar el resultado.

## Parche previo al push: aplicado

- Ocho TTF (3.912.124 bytes) sustituidos por cinco subconjuntos (536.336 bytes).
- Se conserva Sans-BoldOblique para títulos en cursiva; Mono usa solo normal.
- Validación contra la fuente efectiva de cada fragmento, con línea real de error.
- No se examinan glifos de URLs o rutas que no se imprimen.
- Dimensiones del resumen leídas del PNG guardado; prueba con figsize y dpi distintos.
- 14 pruebas, fuente y hashes documentados, salidas de referencia actualizadas.
- PARCHE-FUENTES.md enumera exactamente las tres fuentes antiguas que retirar.

La siguiente tanda prioriza tarjeta social/JSON-LD, después devcontainer y
comprobación del entorno, y después publicación propia con URL base derivada.
Galería, Discussions y mantenimiento periódico quedan para después de la charla.

## Corrección posterior al push: imagen identificada por contenido

- El PDF identificaba cada imagen con un nombre derivado de su ruta absoluta
  (`FormXob.<hash>`), de modo que dos copias del repositorio en carpetas
  distintas producían documentos con bytes distintos y el mismo contenido.
- `crear_pdf.py` entrega ahora los bytes de la imagen a ReportLab. El resultado
  no depende de la ubicación del clon ni del directorio de trabajo.
- Prueba añadida: el mismo Markdown e imagen, generados desde dos carpetas
  temporales con nombres distintos, producen PDF idénticos. 15 pruebas.
- `ejemplos/salida-esperada/informe.pdf` se regenera con este cambio.
- Queda disponible, si se desea, comparar en Actions una ejecución nueva con la
  salida de referencia; conviene generar esa referencia en el mismo entorno.

## Documentos de entrega ya cumplidos

`PUBLICAR.md`, `ACTUALIZAR.md` y `PARCHE-FUENTES.md` describen migraciones
terminadas. Consolidar su parte vigente (publicación, Zenodo, mantenimiento de
fuentes) en un único documento, o moverlos a `docs/`, deja la raíz más clara
para quien copie la plantilla.
