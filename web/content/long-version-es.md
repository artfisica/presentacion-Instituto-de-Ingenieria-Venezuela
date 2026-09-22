# De los datos abiertos al conocimiento compartido

Instituto de Ingeniería · Venezuela · Charla en línea

**Te llevas un repositorio que funciona.**

Este mismo repositorio reúne tres ejercicios: analizar datos, crear un gráfico y generar un PDF automáticamente desde Markdown e imágenes. Puedes clonarlo, ejecutar los scripts y empezar tus propios prototipos. Si puedes y quieres, llega a la charla con tu cuenta de GitHub creada.

Investigar y enseñar suele exigir mucho más que analizar datos: hay que preparar un entorno, escribir scripts, ordenar archivos, registrar decisiones y mantener actualizados gráficos, informes y materiales. Esta charla muestra cómo conectar esas tareas en un proceso sencillo que permita dedicar más tiempo a las preguntas y a la interpretación de los resultados.

Los participantes aprenderán para qué sirven Git y GitHub al conservar versiones de código, datos y documentos; cómo usar scripts de Python para repetir un análisis; y cómo automatizar tareas con GitHub Actions. Un cambio en los datos puede producir un nuevo gráfico; un cambio en un texto Markdown o en una imagen puede generar un nuevo PDF. Cada resultado queda asociado a la versión de los archivos que lo produjo.

El repositorio de esta misma presentación será también el material práctico que cada participante podrá clonar o copiar en su cuenta. Contiene carpetas sencillas para datos, ejemplos, imágenes y ejercicios, junto con tres actividades guiadas: **analizar un CSV, crear un gráfico y generar un PDF desde Markdown e imágenes**. Se puede empezar cambiando un valor, un título o una fotografía, y adaptar después el ejemplo a una tesis, una clase o un proyecto comunitario.

Se discutirá también cómo utilizar cuadernos de análisis, notas y modelos de lenguaje para comprender código, preparar scripts y documentar el trabajo, comprobando sus resultados. El objetivo es aprender a aprovechar recursos disponibles con criterio, reconocer qué tareas se repiten entre proyectos y convertir una solución particular en un punto de partida que otras personas puedan reutilizar. Si puedes y quieres, llega a la charla con tu cuenta de GitHub creada.

## ATLAS Open Data

Datos experimentales, software, documentación y acompañamiento para realizar investigación y formación universitaria desde Venezuela. Las tesis de Iskya, María y Oscar conectan estas herramientas con proyectos en la UCV y la ULA.

Iskya García desarrolló su maestría en la UCV, bajo la supervisión de Arturo, estudiando candidatos a materia oscura con datos abiertos de ATLAS y simulaciones. María Di Domenico realizó su licenciatura en la UCV reconstruyendo masas de los bosones W, Z y Higgs con ROOT, Jupyter y SWAN. Sus resultados también se convirtieron en recursos educativos reutilizables. <strong>Oscar Alejandro Altuve Pabon (ULA)</strong> defendió su tesis de licenciatura el 1 de febrero de 2022, bajo la supervisión de Arturo Sánchez y Alberto Patiño. Estudió la optimización del análisis de Higgs en el canal H → ZZ* → 4ℓ a 13 TeV con ATLAS Open Data, ROOT/C++ y Jupyter. El trabajo se desarrolló en una máquina virtual para ejecutar los análisis localmente con menor dependencia de internet. El material está preservado en Zenodo y enlaza su código.

[Explorar los datos](https://opendata.atlas.cern/) · [Iskya y María en ATLAS](https://atlas.cern/updates/blog/HEP-education-worldwide-with-atlas-open-data) · [Tesis de Iskya](https://cds.cern.ch/record/2291838/) · [Tesis de María](https://cds.cern.ch/record/2293251/) · [Tesis de Oscar (ULA)](https://zenodo.org/records/18372123) · [Código de Oscar](https://github.com/AltuOs/HZZ4l/releases/tag/v2.0.0)

## De una memoria USB a infraestructura compartida

Acercar la infraestructura al estudiante es una línea de trabajo de años: llevar entornos listos para usar y facilitar que una institución los adapte a sus recursos.

En CHEP 2018, Arturo presentó ATLAS Open Data y Open Key: datos, software, notebooks y documentación transportables en una memoria USB, con máquinas virtuales para trabajar donde la conectividad es limitada. Las diapositivas muestran su aplicación a formación y tesis en Venezuela. En 2021, Arturo Sánchez Pineda y Giovanni Guerrieri publicaron una propuesta de despliegue multiusuario con JupyterHub e infraestructura como código. Documenta una primera prueba con Terraform y OpenStack en CERN; los demás escenarios se presentan como propuestas. Para esta charla, el aprendizaje es práctico: entregar un entorno reproducible reduce el trabajo de instalación que cada estudiante debe repetir.

[Contribución CHEP 2018](https://indico.cern.ch/event/587955/contributions/2938491/) · [Diapositivas de 2018 (PDF)](https://indico.cern.ch/event/587955/contributions/2938491/attachments/1635910/2689773/CHEP_2018_Arturo_Sanchez_ATLAS_Open_Data.pdf) · [Artículo de 2021 (PDF)](https://cds.cern.ch/record/2772504/files/epjconf_chep2021_01008.pdf) · [DOI del artículo](https://doi.org/10.1051/epjconf/202125101008)

## Hackatón CoAfina

Estudiantes de distintos países y disciplinas se reúnen para resolver retos con datos abiertos, acompañados por mentores y una comunidad de aprendizaje.

Coorganizado desde sus comienzos, CoAfina combina trabajo colaborativo, repositorios, documentación y presentación pública de resultados. Una actividad intensiva se convierte en proyectos reutilizables y relaciones que continúan después del evento. Creative Commons Venezuela, LA-CoNGA Physics, RedCLARA y CEDIA han formado parte de esta experiencia.

[Conocer CoAfina](https://laconga.redclara.net/hackathon/) · [Materiales en GitHub](https://github.com/laa-hecap/CoAfina-resources)

## LAGO Mérida

Reutilizar equipos disponibles como recursos compartidos para estudiantes e investigadores: enviar un trabajo y recuperar resultados reproducibles.

La propuesta plantea cómputo remoto con flujos automatizados que devuelven gráficos, informes y registros de ejecución. Es un servicio acotado para docencia y trabajos modestos, con responsabilidades claras sobre acceso, preservación y publicación de datos. El proyecto muestra cómo ampliar capacidades locales con recursos existentes.

[Ver la propuesta y el código](https://github.com/laa-hecap/LAGO-merida-infra) · [Conocer LAGO](https://lagoproject.net/)

## Callejero Villa Yacanto

Un problema de la comunidad se convierte en una experiencia para revisar fuentes, registrar dudas y proponer cambios con trazabilidad.

El flujo de trabajo utiliza GitHub y Codespaces para revisar un inventario de calles. Las contribuciones pasan por verificaciones automáticas y revisión humana. El estudiante aprende a explicar una decisión y a conservar la evidencia que la respalda; la validación técnica y la decisión municipal tienen responsabilidades distintas.

[Abrir el proyecto](https://los-topos-cosmicos.github.io/callejero-yacanto/) · [Explorar el repositorio](https://github.com/los-topos-cosmicos/callejero-yacanto)

## Beam4School

Propuestas experimentales, simulaciones configurables y documentación reunidas en un proyecto que los estudiantes pueden explorar y mejorar.

El objetivo es ofrecer un punto de entrada accesible a herramientas científicas exigentes. Los estudiantes relacionan los parámetros que eligen con los resultados obtenidos y documentan su razonamiento, mientras aprenden progresivamente la computación que sostiene el experimento.

[Explorar Beam4School](https://github.com/los-topos-cosmicos/beam4school-proposal)

## Mapa Civil / Reality Map

Un proyecto bilingüe para examinar cuestiones geopolíticas mediante estudios, fuentes y un registro de afirmaciones que el lector puede inspeccionar.

El método distingue acontecimientos documentados, decisiones judiciales, hallazgos, posiciones oficiales, inferencias y pronósticos. La documentación versionada, las verificaciones y la publicación estática trasladan prácticas de reproducibilidad al análisis cívico. Las herramientas de IA pueden asistir; la clasificación y la revisión siguen en manos de personas.

[Leer los estudios](https://artfisica.github.io/reality-map/es/) · [Ver el repositorio](https://github.com/artfisica/reality-map)

## SILAFAE y CSC Chile

Programación, control de versiones, pruebas, documentación, depuración y rendimiento conectados mediante ejercicios prácticos.

El aprendizaje avanza desde obtener un resultado correcto hasta colaborar en su desarrollo y mejorar su ejecución. Los materiales de SILAFAE y de la CERN School of Computing en Chile pueden reutilizarse en otros cursos, tesis y proyectos científicos.

[Ejercicios CSC 2026](https://github.com/artfisica/csc2026) · [Taller SILAFAE](https://github.com/laa-hecap/workshop-silafae-2024) · [La escuela en Chile](https://indico.cern.ch/event/1551289/)

## Conocimiento abierto en acción

Organizar comunidades para transformar evidencia científica en contenidos públicos y reutilizables, con reconocimiento de fuentes y autoría.

Desde Creative Commons Venezuela se han impulsado alianzas, hackatones y editatones. Salud para todos, realizado con la OMS, Cornell y comunidades de conocimiento abierto, reunió expertos y voluntarios para trabajar en Wikipedia. La experiencia dio lugar a una publicación científica en 2026.

[Leer la publicación](https://www.alanrevista.org/ediciones/2026/1/art-6) · [Creative Commons y Arturo](https://creativecommons.org/2021/08/24/meet-the-cc-summit-presenter-arturo-sanchez-pineda/)

## CEVALE2VE y LA-CoNGA

Cooperación entre investigadores, docentes e instituciones para acercar formación y recursos educativos a estudiantes latinoamericanos.

Estas experiencias permiten examinar cómo sostener cursos, proyectos y vínculos académicos entre personas ubicadas en distintos países. El valor está en conectar infraestructura, materiales y acompañamiento humano para que el conocimiento pueda circular y mantenerse.

[El caso CEVALE2VE](https://cds.cern.ch/record/2241903/) · [LA-CoNGA Physics](https://laconga.redclara.net/)

## Resolver una vez. Compartir lo aprendido.

La automatización permite ejecutar análisis, verificar cambios y generar informes de forma consistente. Las notas, los scripts, los datos y los documentos quedan conectados con las decisiones que llevaron a cada resultado.

El principio que conecta estas experiencias es la **generalización de soluciones**: identificar necesidades comunes y desarrollar métodos que otros grupos puedan adaptar. Esta visión está recogida en las contribuciones a LAA-HECAP y LASF4RI, particularmente en la [propuesta de estrategias y servicios computacionales transversales para investigación y formación](https://zenodo.org/records/13324266).

## Aprovechar lo disponible. Conservar el criterio.

La presentación abordará cómo aprovechar plataformas como GitHub, parte de Microsoft, junto con herramientas abiertas e infraestructura académica. El interés es práctico y crítico: saber qué ofrecen, bajo qué condiciones y cómo mantener el trabajo documentado y trasladable a otros entornos.

Los **modelos de lenguaje** pueden ayudar a explicar código, preparar borradores de scripts, proponer pruebas, mejorar documentación, adaptar materiales educativos y apoyar la lectura de textos. Su utilidad depende de formular bien las tareas, contrastar las fuentes y comprobar los resultados. El razonamiento, la autoría y la validación siguen siendo responsabilidad de las personas.

La charla está dirigida a estudiantes, docentes, investigadores y personas que impulsan proyectos científicos, educativos o comunitarios. El objetivo es ofrecer ejemplos y métodos adaptables en Venezuela y la región: hacer que los recursos disponibles se conviertan en autonomía para aprender, investigar y producir conocimiento compartido.

## Arturo Sánchez Pineda

Arturo Sánchez Pineda es físico venezolano, profesional de la ingeniería de infraestructura y educador. Su formación comenzó en la Universidad de Los Andes, en Mérida, donde cursó estudios de Física e Ingeniería y obtuvo su licenciatura en Física con distinción Magna Cum Laude. Continuó su formación investigadora en el LPNHE de la Université Paris-Diderot mediante el programa HELEN y obtuvo su doctorado en Física de Altas Energías en la Universidad de Nápoles Federico II en 2013. Su investigación doctoral se centró en la búsqueda del bosón de Higgs con ATLAS. [Trayectoria académica](https://twiki.org/p/pub/Main/ArturoSanchez/Arturo_Sanchez_Curriculum_June_2016.pdf).

Su carrera científica incluye investigación y responsabilidades de computación en Nápoles e INFN, trabajo posdoctoral vinculado al ICTP, la Universidad de Udine e INFN, y desarrollo de infraestructura científica en LAPP dentro del proyecto europeo ESCAPE. Ha trabajado en análisis de datos de física de partículas, software científico, procesamiento distribuido y herramientas para facilitar el trabajo de otros investigadores.

Formó parte de la colaboración ATLAS durante el descubrimiento del bosón de Higgs en 2012. El descubrimiento realizado por ATLAS y CMS confirmó experimentalmente el mecanismo teórico reconocido con el **Premio Nobel de Física de 2013, otorgado a François Englert y Peter Higgs**. El posterior artículo conjunto sobre la masa del Higgs, publicado en 2015 con 5.154 contribuyentes, fue reconocido por Guinness World Records por su número de participantes. [Nobel de Física](https://www.nobelprize.org/prizes/physics/2013/press-release/) · [Récord Guinness](https://www.guinnessworldrecords.com/world-records/421538-most-contributors-to-a-research-paper).

Fue administrador de sistemas de la infraestructura de selección y adquisición de datos de ATLAS en el CERN, dentro del pequeño equipo especializado responsable de sostener sistemas esenciales para el funcionamiento del experimento. Esta responsabilidad le permitió unir la perspectiva del investigador que necesita analizar datos con la del profesional que mantiene la infraestructura para hacerlo posible.

Como cofundador y coordinador de ATLAS Open Data, contribuyó a acercar datos, software, documentación y formación a estudiantes y docentes fuera de la colaboración. Su trayectoria educativa incluye docencia universitaria, dirección y acompañamiento de trabajos de grado y maestría, formación de estudiantes y participación como profesor en escuelas internacionales, incluida la CERN School of Computing en Chile. [Perfil en ATLAS](https://atlas.cern/authors/arturo-sanchez-pineda).

Es cofundador de CEVALE2VE y del capítulo Creative Commons Venezuela, del que es representante y desde el que impulsa iniciativas de educación y conocimiento abierto. Ha contribuido a LA-CoNGA Physics, coorganiza CoAfina y participa en esfuerzos regionales de LAA-HECAP y LASF4RI para fortalecer la formación y la infraestructura científica. Su trabajo combina coordinación de comunidades, mentoría, licencias abiertas, documentación y producción colaborativa de recursos. [Perfil en Creative Commons](https://creativecommons.org/2021/08/24/meet-the-cc-summit-presenter-arturo-sanchez-pineda/).

Actualmente dirige Infraestructura y Operaciones de TI en INAIT, empresa suiza de inteligencia artificial, donde trabaja en computación en la nube, automatización, seguridad, continuidad operativa y gestión de recursos. Mantiene una actividad científica y educativa mediante publicaciones, proyectos, enseñanza y colaboración internacional. Su artículo de 2026 sobre Salud para todos, como primer autor junto con colaboradores de la OMS y Cornell y con afiliación a INAIT, ofrece un ejemplo concreto de esa continuidad entre industria, investigación y conocimiento abierto. [Publicación](https://www.alanrevista.org/ediciones/2026/1/art-6).

El hilo conductor de su trayectoria es convertir experiencia técnica especializada en herramientas y oportunidades que otras personas puedan utilizar: acercar la infraestructura al estudiante y al investigador, automatizar tareas repetitivas y desarrollar soluciones reutilizables que mantengan el rigor científico y sean sencillas de adoptar.
