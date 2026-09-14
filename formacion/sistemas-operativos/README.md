# Sistemas operativos, administración y ciberseguridad

**Wiktor Nykiel · Edición 1.1 · Español · Distribución privada · 14 de septiembre de 2026.**

Programa independiente para aprender a comprender, operar, proteger, automatizar e investigar sistemas Linux, Windows y macOS. Se comienza con archivos, terminal y funcionamiento del SO; se termina integrando administración, evidencias, recuperación y comunicación. Predomina la terminal, con GUI para comprender y contrastar resultados.

## Empezar por una actividad real

Abrir [Inicio rápido](INICIO-RAPIDO.md), preparar una carpeta sintética y completar [R01: archivos](practicas/R01-archivos.md). Después seguir [el plan docente](PLAN-DOCENTE.md) y [el laboratorio](LABORATORIO.md). El kit es material de apoyo: un alumno inicial no necesita saber Python para utilizar un dataset preparado por el docente.

| Recurso | Qué contiene |
|---|---|
| [Lecciones desarrolladas](lecciones/README.md) | Ocho capítulos con explicación, ejemplos, errores y preguntas de defensa |
| [Prácticas paso a paso](practicas/README.md) | Ocho runbooks vinculados a laboratorios del programa, con resultados, variantes y recuperación |
| [Kit ejecutable](kit/README.md) | Datos sintéticos, herramientas offline, ejemplos Bash/BAT/PowerShell/zsh y servicio web de laboratorio |
| [Planificación verificable](planificacion/README.md) | Catálogo de 32 módulos y generación de 240 sesiones y 96 laboratorios |
| [Resultados de validación](qa/RESULTADOS.md) | Pruebas ejecutadas, versiones, alcance y limitaciones |
| [Cambios de esta edición](CHANGELOG.md) | Diferencias entre diseño curricular y material ejecutable añadido |

## Programa completo: 480 horas

| Bloque | Módulos | Horas | Desarrollo curricular |
|---|---|---:|---|
| Fundamentos, laboratorio y método | M01–M04 | 56 | [Fundamentos](modulos/01-fundamentos.md) |
| Linux y Bash | M05–M12 | 112 | [Linux](modulos/02-linux.md) |
| Windows, CMD, BAT y PowerShell | M13–M19 | 98 | [Windows](modulos/03-windows.md) |
| macOS, Darwin y zsh | M20–M23 | 56 | [macOS](modulos/04-macos.md) |
| Operación multiplataforma y ciberseguridad | M24–M30 | 98 | [Operación y seguridad](modulos/05-operacion-seguridad.md) |
| IA desde terminal | M31 | 20 | [IA](modulos/06-ia.md) |
| Proyecto integrador y defensa | M32 | 40 | [Capstone](CAPSTONE.md) |
| **Total** | **32** | **480** | **168 de teoría y 312 de práctica** |

Se mantienen los 96 laboratorios diseñados, tres por módulo. Los ocho runbooks nuevos concretan una selección de ellos; no son horas ni laboratorios adicionales. Las rutas abreviadas de 60, 120 y 240 horas siguen definidas en el plan docente, con alcance diferenciado.

## Aprender, comprobar, explicar

Cada práctica pide identificar sistema, versión, identidad, directorio y efecto esperado; utilizar privilegios mínimos; conservar datos originales; verificar un resultado positivo y uno negativo; y documentar reversión. Se propone resolver o verificar por CLI al menos el 80 % de las tareas prácticas evaluables, con adaptaciones de accesibilidad.

Los ejemplos de Bash, BAT, PowerShell y zsh operan sobre el mismo dataset para comparar modelos y límites, no para fingir que los sistemas son iguales. Windows nativo es necesario para Registro, NTFS, Event Log y administración de Windows. macOS nativo es necesario para APFS, launchd, TCC y controles Apple. PowerShell en Linux no sustituye esas comprobaciones.

La perspectiva Red/Purple se trabaja mediante revisión de permisos y superficie, relaciones de confianza, segmentación, pruebas benignas y retest. La investigación utiliza evidencia sintética; no contiene instrucciones de intrusión, evasión ni extracción de credenciales. La IA propone y explica: no ejecuta automáticamente, no recibe secretos y no valida por sí sola sus conclusiones.

## Estado real de esta entrega

**50 pruebas automatizadas ejecutadas en Linux: 42 del kit/HTTP local y 8 de planificación**, además de comprobación sintáctica Bash. Los scripts nativos Windows/PowerShell y zsh/macOS están escritos y documentados, pero no ejecutados en sus plataformas. Los manifiestos Docker/Compose/Swarm están preparados, no desplegados ni certificados.

No se afirma haber ejecutado los 96 laboratorios completos, ni impartido 480 horas, ni validado una cohorte. El servicio HTTP es exclusivamente didáctico, sin autenticación/TLS y no apto para producción. Consultar [validación](VALIDACION.md) y [resultados](qa/RESULTADOS.md) antes de reutilizarlo.

## Material docente y de consulta

[Guía del docente](GUIA-DOCENTE.md) · [Competencias y perfiles](COMPETENCIAS.md) · [Evaluación](EVALUACION.md) · [Banco de preguntas](BANCO-PREGUNTAS.md) · [Equivalencias por sistema](REFERENCIA-CRUZADA.md) · [Guías rápidas](CHEATSHEETS.md) · [Bastionado](BASTIONADO.md) · [Plantillas](PLANTILLAS.md) · [Fuentes](FUENTES.md) · [Uso responsable](USO-RESPONSABLE.md).

Los materiales están autocontenidos en este directorio y no necesitan ejecutar ni modificar la aplicación de la raíz del repositorio. No se activa publicación web, GitHub Pages, nuevos colaboradores o despliegues automáticos. Antes de compartir con alumnos, separar soluciones y expedientes mediante permisos reales: una carpeta no constituye una frontera de acceso.

Materiales propios reservados para el titular. Las referencias externas conservan sus licencias; no se redistribuyen instaladores, imágenes o manuales de terceros.
