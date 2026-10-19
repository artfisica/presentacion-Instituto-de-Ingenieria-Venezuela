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
- Sala concreta de FORMATEC cuando la indique la organización: `EVENT['room']` y
  `EVENT['room_link']` en `web/content/site.py`, seguido de `python3 web/build.py`.
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

## Fecha confirmada: aplicada

- Charla confirmada para el miércoles 21 de octubre de 2026 a las 9:00 a. m., hora de
  Venezuela (UTC−4; 13:00 UTC). Los datos viven solo en `EVENT`, en
  `web/content/site.py`; `build.py` genera con ellos la cápsula de la portada, el
  pie de página, las versiones extensas y los calendarios `charla.ics` y `talk.ics`
  en `web/assets/` (hora en UTC, DTSTAMP fijo, líneas plegadas a 75 octetos).
- Conexión confirmada el 19 de octubre: las Salas Virtuales FORMATEC del Instituto
  de Ingeniería (`EVENT['link']`), enlazadas desde la cápsula, el pie de página,
  las versiones extensas, README, Telegram y los `.ics` (como ubicación). La sala
  concreta sigue pendiente: al escribirla en `EVENT['room']` y `EVENT['room_link']`,
  aparece junto al enlace y el `.ics` pasa a usar la sala como ubicación.
- La duración del calendario es una estimación de 60 minutos (`EVENT['minutes']`).
- `validate.py` comprueba los dos `.ics` y que su hora coincida con `EVENT`.
- La edición manual previa de `index.html` y `en.html` no llegaba a la web: `pages.yml`
  regenera ambos desde `site.py` antes de publicar. Queda documentado en README.
- README y `telegram-es.md` incluyen la fecha, la hora y el enlace al calendario.

## Documentos de entrega ya cumplidos

`PUBLICAR.md`, `ACTUALIZAR.md` y `PARCHE-FUENTES.md` describen migraciones
terminadas. Consolidar su parte vigente (publicación, Zenodo, mantenimiento de
fuentes) en un único documento, o moverlos a `docs/`, deja la raíz más clara
para quien copie la plantilla.
