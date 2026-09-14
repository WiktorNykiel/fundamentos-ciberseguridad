# Sistemas operativos, administración y ciberseguridad

**Wiktor Nykiel · Edición documental 1.2 · Español · 14 de septiembre de 2026.**

Programa independiente para comprender, operar, proteger, automatizar e investigar sistemas Linux, Windows y macOS. Se comienza con archivos, terminal y funcionamiento del SO; se termina integrando administración, evidencias, recuperación y comunicación. Predomina la terminal, con GUI para comprender y contrastar resultados.

**Difusión pública solicitada por el titular.** El cambio de visibilidad del repositorio requiere una operación administrativa distinta de guardar o fusionar archivos. El estado y los materiales preparados están en [Publicación y distribución](PUBLICACION.md); no se debe interpretar esta cabecera como prueba de acceso anónimo.

## Empezar por una actividad real

Abrir [Inicio rápido](INICIO-RAPIDO.md), preparar una carpeta sintética y completar [R01: archivos](practicas/R01-archivos.md). Después seguir [el plan docente](PLAN-DOCENTE.md) y [el laboratorio](LABORATORIO.md). Un alumno inicial no necesita programar en Python para trabajar con datos preparados por el docente.

| Recurso | Contenido |
|---|---|
| [Lecciones desarrolladas](lecciones/README.md) | Ocho capítulos con explicaciones, ejemplos y preguntas de defensa. |
| [Prácticas paso a paso](practicas/README.md) | Ocho runbooks del kit del repositorio, vinculados al programa. |
| [Kit del repositorio](kit/README.md) | Datos sintéticos, herramientas offline, Bash/BAT/PowerShell/zsh y servicio web de laboratorio. |
| [Planificación verificable](planificacion/README.md) | Catálogo de 32 módulos y generación de 240 sesiones y 96 laboratorios. |
| [Ampliación práctica 1.1 para alumnos](PUBLICACION.md) | Paquete separado con 16 guías ampliadas, scripts, 64 preguntas sin soluciones y planificación XLSX/JSON/CSV. |
| [Resultados del kit del repositorio](qa/RESULTADOS.md) | Registro histórico de sus pruebas, versiones y límites. |
| [Cambios anteriores](CHANGELOG.md) | Desarrollo del material ejecutable y del diseño curricular. |

## Fundamentos y administración de sistemas: 322 horas

| Bloque | Horas | Contenido principal |
|---|---:|---|
| **[Fundamentos y método](modulos/01-fundamentos.md)** | **56** | Bits y bytes, codificaciones, hardware, arquitectura del SO, procesos, memoria, almacenamiento, laboratorio, terminal, documentación y Git. |
| **[Linux y Bash](modulos/02-linux.md)** | **112** | Directorios y archivos, búsquedas y pipelines, usuarios, permisos y ACL, procesos, paquetes, servicios, tareas, almacenamiento, copias, redes y scripting robusto. |
| **[Windows, CMD, BAT y PowerShell](modulos/03-windows.md)** | **98** | Administración GUI y CLI, arquitectura y Registro, utilidades nativas, lotes, objetos y datos, servicios, permisos NTFS, identidad, acceso remoto, eventos y recuperación. |
| **[macOS, Darwin y zsh](modulos/04-macos.md)** | **56** | APFS, rutas y metadatos, Finder y Terminal, diferencias Bash/zsh, preferencias, usuarios, launchd, servicios, redes, seguridad de plataforma y evidencias. |
| **Subtotal de los cuatro bloques** | **322** | **M01–M23.** |

## Integración y especialización: 158 horas

| Bloque | Horas | Contenido principal |
|---|---:|---|
| [Operación multiplataforma y ciberseguridad](modulos/05-operacion-seguridad.md) | 98 | M24–M30: redes, acceso remoto, transferencias, web/TLS, contenedores, observabilidad, DFIR, IOCs/CTI y evaluación de controles. |
| [IA desde terminal](modulos/06-ia.md) | 20 | M31: revisión de scripts y logs, propuestas estructuradas, privacidad y validación humana. |
| [Proyecto integrador](CAPSTONE.md) | 40 | M32: construir, operar, bastionar, investigar, recuperar y defender una solución. |
| **Subtotal** | **158** | No sustituye los cuatro bloques de sistemas. |
| **Programa completo** | **480** | **32 módulos · 168 horas de teoría · 312 horas de práctica.** |

Se mantienen 96 laboratorios diseñados, tres por módulo, y 240 sesiones de dos horas. Los runbooks y las guías ampliadas concretan laboratorios existentes: no añaden horas automáticamente. Las rutas de 60, 120 y 240 horas tienen alcance diferenciado en el plan docente.

## Aprender, comprobar y explicar

Cada práctica pide identificar sistema, versión, identidad, directorio y efecto; utilizar privilegios mínimos; conservar originales; verificar resultados positivos y negativos; y documentar recuperación. Se propone resolver o verificar por CLI al menos el 80 % de las tareas prácticas evaluables, con adaptaciones de accesibilidad.

Linux, Windows y macOS se trabajan como plataformas reales. PowerShell en Linux no valida Registro, NTFS, Event Log o administración nativa de Windows. Un contenedor Linux no valida APFS, launchd, TCC o controles de Apple. Los ejemplos de los distintos lenguajes permiten comparar contratos y diferencias, no fingir equivalencia entre sistemas.

La perspectiva Red/Purple utiliza revisión de permisos y superficie, confianza, segmentación, pruebas benignas y retest. La investigación usa evidencia sintética. La IA propone y explica; no recibe secretos, ejecuta automáticamente ni valida por sí sola sus conclusiones.

## Validación: dos conjuntos de material distintos

El kit integrado en `kit/` conserva su informe histórico de **50 pruebas** en [qa/RESULTADOS.md](qa/RESULTADOS.md). La ampliación descargable utiliza otro motor, otros scripts y sus propios fixtures: **75 pruebas locales correctas** al volver a verificar el paquete para alumnos el 14 de septiembre de 2026. No se suman ambas cifras como si representasen cobertura única ni se mezclan sus datasets o comandos.

Los scripts nativos Windows/PowerShell/BAT y macOS/zsh necesitan ejecución en sus plataformas. Docker/Compose/Swarm están preparados, no desplegados. No se afirma haber ejecutado los 96 laboratorios completos, impartido 480 horas o validado una cohorte. El servidor HTTP es didáctico, no una plataforma de producción.

## Material de consulta

[Guía docente](GUIA-DOCENTE.md) · [Competencias](COMPETENCIAS.md) · [Evaluación](EVALUACION.md) · [Preguntas introductorias](BANCO-PREGUNTAS.md) · [Equivalencias por sistema](REFERENCIA-CRUZADA.md) · [Guías rápidas](CHEATSHEETS.md) · [Bastionado](BASTIONADO.md) · [Plantillas](PLANTILLAS.md) · [Fuentes](FUENTES.md) · [Uso responsable](USO-RESPONSABLE.md).

El curso no necesita ejecutar la aplicación de la raíz. Los expedientes, las respuestas de evaluación y las comunicaciones privadas no deben publicarse. La copia para alumnos se distribuye sin el directorio de soluciones docentes ni el libro original con respuestas. Una carpeta o una rama dentro de un repositorio público no constituye control de acceso.

No se asigna automáticamente una nueva licencia libre. Los materiales propios y las referencias externas conservan sus derechos y licencias; no se redistribuyen instaladores, imágenes ni manuales completos de terceros.
