# Sistemas operativos, administración y ciberseguridad

**Autor y responsable editorial: Wiktor Nykiel.** Edición curricular 1.0 · 14 de septiembre de 2026 · Español · Distribución privada.

Programa independiente, desde iniciación hasta administración intermedia-avanzada. Linux, Windows y macOS se trabajan como sistemas reales, no como comandos intercambiables. El hilo conductor es construir, operar, proteger, automatizar e investigar una pequeña infraestructura, documentando cada decisión.

## Empezar

1. Leer [el plan docente](PLAN-DOCENTE.md) y realizar el diagnóstico inicial.
2. Preparar [el laboratorio](LABORATORIO.md), aprobar sus controles de aislamiento y registrar las versiones.
3. Recorrer los módulos en orden y entregar los laboratorios identificados como `L01A` a `L32C`.
4. Consultar [las equivalencias](REFERENCIA-CRUZADA.md), [las guías de terminal](CHEATSHEETS.md), [las rúbricas](EVALUACION.md) y [las plantillas](PLANTILLAS.md).
5. Defender [el proyecto final](CAPSTONE.md) con funcionamiento, recuperación y evidencias, no solo capturas.

## Contenido

| Bloque | Módulos | Horas | Documento |
|---|---|---:|---|
| Fundamentos, laboratorio y método | M01–M04 | 56 | [Fundamentos](modulos/01-fundamentos.md) |
| Linux y Bash | M05–M12 | 112 | [Linux](modulos/02-linux.md) |
| Windows, CMD, BAT y PowerShell | M13–M19 | 98 | [Windows](modulos/03-windows.md) |
| macOS, Darwin y zsh | M20–M23 | 56 | [macOS](modulos/04-macos.md) |
| Operación multiplataforma y ciberseguridad | M24–M30 | 98 | [Operación y seguridad](modulos/05-operacion-seguridad.md) |
| IA desde terminal | M31 | 20 | [IA](modulos/06-ia.md) |
| Proyecto integrador y defensa | M32 | 40 | [Capstone](CAPSTONE.md) |
| **Total** | **32** | **480** | **168 de teoría y 312 de práctica** |

Los módulos M01–M30 tienen 14 horas cada uno: 5 de teoría y 9 de práctica. M31 tiene 8+12 y M32 tiene 10+30. Se diseñan **96 laboratorios**, tres por módulo. En M32 son tres fases integradoras. Las horas de trabajo, evaluación y preparación descritas dentro de cada módulo ya están incluidas; no se suman de nuevo.

## Qué se entrega y qué no se afirma

Esta edición contiene un temario desarrollado, objetivos medibles, unidades, prácticas diseñadas, herramientas, entregables, criterios de éxito, evaluación, proyecto final y referencias. No es una colección de máquinas virtuales ni una plataforma LMS. Las prácticas nativas de Windows y macOS necesitan su sistema correspondiente. Un contenedor Linux con PowerShell no valida NTFS, Registro, Event Log, WinRM, Active Directory o controles de Apple.

Los laboratorios son **diseños docentes**, pendientes de ejecución y ajuste por el docente sobre las imágenes concretas de la cohorte. La revisión de documentación no equivale a haber ejecutado todos los comandos ni a una certificación de seguridad. Consultar [validación y mantenimiento](VALIDACION.md).

## Principios

Predominio de terminal: al menos el 80 % de las tareas prácticas evaluables se resuelve o verifica mediante CLI. La GUI se utiliza para formar un modelo mental, localizar controles y contrastar resultados. No se penaliza la accesibilidad: puede utilizarse una interfaz equivalente si demuestra la misma competencia.

Seguridad transversal: mínimo privilegio, cambios reversibles, datos sintéticos, trazabilidad, copias verificadas y separación entre observar y modificar. La formación para Red Team aborda planificación autorizada, análisis de superficie, permisos, segmentación y evaluación de controles. Los conceptos de pivotaje se estudian mediante diagramas y telemetría, no mediante instrucciones para comprometer equipos o eludir controles.

La IA propone y explica; no recibe credenciales, no aprueba sus propias acciones y no ejecuta automáticamente texto obtenido de logs, documentos o Internet.

## Documentación complementaria

- [Matriz de competencias y perfiles](COMPETENCIAS.md).
- [Banco de preguntas y soluciones orientativas](BANCO-PREGUNTAS.md).
- [Bastionado y recuperación](BASTIONADO.md).
- [Fuentes primarias y versiones](FUENTES.md).
- [Uso responsable](USO-RESPONSABLE.md).
- [Guía del docente y secuenciación](GUIA-DOCENTE.md).

## Ubicación y conservación

El curso está autocontenido en este directorio. No modifica ni necesita ejecutar la aplicación que pueda existir en la raíz del repositorio. Puede trasladarse íntegramente a otro repositorio privado conservando sus enlaces relativos. No se habilitan publicación web, GitHub Pages, nuevos colaboradores ni automatizaciones de despliegue.

Los materiales propios permanecen reservados para el titular. Las referencias externas conservan sus licencias y condiciones; no se redistribuyen manuales, benchmarks, instaladores o imágenes de terceros.
