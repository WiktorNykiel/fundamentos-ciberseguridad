# Fundamentos de ciberseguridad

> **Este campus se ha trasladado a SmartKEA.** El repositorio público mantenido es [smartkea-cyberinnovation/fundamentos-ciberseguridad](https://github.com/smartkea-cyberinnovation/fundamentos-ciberseguridad) y la web continúa en [smartkea.com/introduccion-ciberseguridad/](https://smartkea.com/introduccion-ciberseguridad/). Los contenidos actuales y sus futuras actualizaciones se encuentran en el nuevo repositorio. Este repositorio conserva el código anterior y su historial como referencia; la [nota de migración](https://github.com/smartkea-cyberinnovation/fundamentos-ciberseguridad/blob/main/docs/MIGRATION.md) documenta el snapshot trasladado y su alcance.

**Wiktor Nykiel · Campus 2.3 · Linux, Windows y macOS · Español e inglés**

Campus de SmartKEA: **https://smartkea.com/introduccion-ciberseguridad/**. El código público se conserva en [WiktorNykiel/fundamentos-ciberseguridad](https://github.com/WiktorNykiel/fundamentos-ciberseguridad).

Aprende a comprender, administrar, automatizar, proteger e investigar sistemas. El curso combina teoría, terminal, prácticas guiadas y evidencias. Los materiales son públicos; las horas describen planificación, no una acreditación automática.

## Ampliación curricular y próxima entrega

El [plan maestro](formacion/plan-maestro/README.md) estructura **18 áreas y 108 unidades propuestas**, desde introducción a la informática hasta cloud, contenedores, gobierno, riesgos, AppSec, Blue Team, CTI y resiliencia. Añade diseños de laboratorio, correspondencias parciales CSF–RGPD–ISO–ENS, un caso numérico de riesgo y un glosario de 110 entradas ES/EN.

Es una **referencia de desarrollo**, no un nuevo catálogo activo ni horas adicionales ya impartidas. Conserva los 32 módulos, 96 fichas y 480 horas actuales. Las instrucciones para continuar, el bilingüismo completo, la accesibilidad móvil y el traspaso seguro de progreso están en [Continuación](formacion/plan-maestro/08-continuacion.md). Hay un [resumen en inglés](formacion/plan-maestro/OVERVIEW.en.md); no se presenta como traducción integral del curso.

## Publicar sin confundir las aplicaciones

El Worker `fundamentos-ciberseguridad` sirve únicamente la subruta del campus. Workers Builds usa la raíz del repositorio, build command vacío, deploy `python3 campus/cloudflare.py deploy` y preview `python3 campus/cloudflare.py preview`; las variables son `SKIP_DEPENDENCY_INSTALL=1`, `PYTHON_VERSION=3.13.3` y `NODE_VERSION=22.23.2`. El comando de Wrangler fijado ejecuta el build del campus, valida y monta los activos antes de subirlos. No necesita OpenNext ni un servicio `frontend`. La rama `main` activa producción; las demás ramas sólo suben versiones de prueba.

Consulta [el procedimiento de publicación, comprobación y recuperación](campus/WORKERS-RECOVERY.md) para la arquitectura de subruta y los comandos reproducibles. Las rutas del campus y las reglas de redirección tienen una recuperación independiente de la versión del Worker.

Para **Pages**, se mantiene la ruta independiente con raíz `campus`, build `python3 build.py && python3 check_release.py` y salida `dist`. [Configuración completa y diagnóstico](campus/DEPLOY-CLOUDFLARE.md).

```sh
python3 campus/cloudflare.py plan
python3 campus/cloudflare.py build
```

Estos comandos preparan y verifican sin publicar. `dry-run` prueba Wrangler sin upload; `deploy` publica producción y `preview` sube una versión de prueba. No son sinónimos.

## Entradas principales

| Necesidad | Recurso |
|---|---|
| Probar la web en Cloudflare | [Despliegue paso a paso](campus/DEPLOY-CLOUDFLARE.md) |
| Comprender cómo estudiar | [Guía de estudio](formacion/sistemas-operativos/COMO-ESTUDIAR.md) |
| Consultar el temario | [Índice del programa](formacion/sistemas-operativos/README.md) |
| Ampliar informática, arquitectura y ciberseguridad | [Plan maestro y referencia de continuidad](formacion/plan-maestro/README.md) |
| Modificar contenido sin duplicarlo | [Guía de edición](campus/EDICION.md) |
| Revisar pruebas y límites | [Aceptación del campus](campus/QA.md) |
| Operar el laboratorio | [Entorno y aislamiento](formacion/sistemas-operativos/LABORATORIO.md) |

## Mapa de formación

| Bloque | Módulos | Horas |
|---|---|---:|
| [Fundamentos y método](formacion/sistemas-operativos/modulos/01-fundamentos.md) | M01–M04 | 56 |
| [Linux y Bash](formacion/sistemas-operativos/modulos/02-linux.md) | M05–M12 | 112 |
| [Windows, CMD, BAT y PowerShell](formacion/sistemas-operativos/modulos/03-windows.md) | M13–M19 | 98 |
| [macOS, Darwin y zsh](formacion/sistemas-operativos/modulos/04-macos.md) | M20–M23 | 56 |
| [Operación y ciberseguridad](formacion/sistemas-operativos/modulos/05-operacion-seguridad.md) | M24–M30 | 98 |
| [IA desde terminal](formacion/sistemas-operativos/modulos/06-ia.md) | M31 | 20 |
| [Proyecto integrador](formacion/sistemas-operativos/CAPSTONE.md) | M32 | 40 |
| **Total: 168 de teoría y 312 de práctica** | **32 módulos / 96 diseños de laboratorio** | **480** |

El índice permite filtrar por bloque, texto y avance sin duplicar el catálogo. La biblioteca añade una lección de despliegue verificable (D21), conservando D01–D20.

El campus genera lectura, presentación y asistente desde las mismas fuentes. Incluye índice de los 32 módulos, prerrequisitos, búsqueda por varias palabras en módulos y biblioteca, autoevaluaciones, notas y progreso local exportable. Las ocho guías R01–R08 amplían parte de los 96 diseños; no equivalen a 96 ejecuciones validadas.

## Compilar y probar el campus

```sh
python3 campus/build.py
python3 campus/check_release.py
python3 campus/serve.py --port 8788
```

Abrir `http://127.0.0.1:8788`. Usar Python 3.11 o posterior. El campus no necesita npm, Next.js, base de datos, cuentas ni API keys para compilarse o servirse. Node y Playwright se utilizan para pruebas, no en el sitio publicado.

**Cloudflare Pages:** raíz `campus`, framework ninguno, comando `python3 build.py && python3 check_release.py`, salida `dist`, variable `SKIP_DEPENDENCY_INSTALL=1`. El ZIP `campus/pages-ready.zip` contiene solo los activos publicables. Consultar primero la guía de despliegue y elegir integración Git o Direct Upload.

## Estructura del repositorio

```text
campus/                         Web estática, compilador, pruebas y guía de Pages
formacion/sistemas-operativos/   Temario, lecciones, prácticas, kit y evaluación
formacion/plan-maestro/          Ampliación curricular y referencia para continuar
src/                            Aplicación Next.js de referencia, independiente
scripts/                        Comprobaciones de integración e historial
.github/workflows/              Validación del campus, referencias y aplicación
```

La aplicación Next.js anterior se conserva. Su uso y alcance están en [Aplicación de referencia](docs/legacy-app.md). No seleccionar el preset Next.js al desplegar el campus.

El asistente guía ejecución manual: no abre una terminal remota ni ejecuta comandos. El progreso es autodeclarado y local al navegador; exportarlo antes de cambiar de origen o dispositivo. No guardar secretos ni datos personales en las notas. Las respuestas formativas son públicas; no son exámenes reservados. No se otorga automáticamente una licencia nueva a los contenidos.
