# Campus web · Fundamentos de ciberseguridad

**Wiktor Nykiel · Versión 2.1.0 · Español · Interfaz clara**

Campus estático generado desde el temario del repositorio: 32 módulos, 480 horas planificadas, 96 fichas, 32 apuntes y 32 autoevaluaciones públicas. Incluye las ocho guías R01–R08 y una biblioteca de 20 recursos. El contenido diseñado no se presenta como práctica nativa ejecutada.

[Desplegar en Pages](DEPLOY-CLOUDFLARE.md) · [Editar el curso](EDICION.md) · [Cómo estudiar](../formacion/sistemas-operativos/COMO-ESTUDIAR.md) · [Pruebas](QA.md)

## Navegación para aprender

| Ruta | Función |
|---|---|
| `#/empezar` | Orientación, preparación, método y conservación del progreso |
| `#/curso` | Siete bloques y continuación del recorrido |
| `#/temario` | Índice de 32 módulos con horas, prerrequisitos y accesos directos |
| `#/laboratorios` | Catálogo de 96 fichas filtrable por bloque |
| `#/recursos` | Biblioteca interna: referencias y lecciones ampliadas |
| `#/progreso` | Lecturas, prácticas, favoritos, exportación e importación |
| `#/modulo/M05` | Teoría con índice interno, texto ampliable y notas |
| `#/modulo/M05/practicas` | Prácticas del módulo |
| `#/modulo/M05/revision` | Autoevaluación formativa |
| `#/modulo/M05/practica/L05A` | Asistente de cinco fases |

La búsqueda por varias palabras ignora mayúsculas y tildes y consulta módulos y documentos. Los prerrequisitos orientan sin bloquear. Los enlaces antiguos D01–D18 conservan su significado; D19 y D20 incorporan plan docente y guía de estudio.

La presentación reutiliza la teoría: flechas, Escape, pantalla completa cuando se admite y desplazamiento de texto largo. `lectura.html` permite consultar e imprimir sin JavaScript. Las tablas disponen de desplazamiento local y la interfaz se adapta al móvil.

## Compilar y comprobar

Desde la raíz de una copia completa:

```sh
python3 campus/build.py
python3 campus/check_release.py
python3 campus/serve.py --port 8788
```

Abrir `http://127.0.0.1:8788`, no `file://`. Python 3.11+; sin dependencias de producción ni red durante el build. El servidor de previsualización solo escucha en loopback y no es un backend de producción.

Se generan `dist/`, `pages-ready.zip`, `build-info.json` y `SHA256SUMS.txt`. El validador verifica catálogo, activos, cabeceras, hashes y equivalencia ZIP/directorio. `sourceCommit` identifica el checkout cuando Cloudflare o Actions aporta su SHA; no se inventa en compilaciones locales.

**Pages:** raíz `campus`; framework ninguno; comando `python3 build.py && python3 check_release.py`; salida `dist`; `SKIP_DEPENDENCY_INSTALL=1`. El sitio no utiliza la aplicación Next.js de la raíz. La URL válida será la devuelta por Cloudflare tras publicar; un commit no equivale a un despliegue.

## Progreso y asistente: límites

160 hitos autodeclarados: lectura, autoevaluación y tres prácticas por módulo. Las cinco fases deben confirmarse antes de finalizar una práctica. Notas, favoritos y marcas se guardan en localStorage, sin cuentas, cifrado ni sincronización entre dispositivos. Exportar antes de cambiar de dominio o navegador. La importación valida tamaño UTF-8, esquema, IDs y rutas. Evitar editar el mismo módulo en varias pestañas a la vez.

El asistente es una guía editorial, no una terminal ni un modelo de IA. No abre SSH/WinRM/RDP, recibe claves ni ejecuta comandos. La comprobación de R01 compara cifras introducidas manualmente con el dataset oslab.py. Windows y macOS requieren sus sistemas nativos. Las marcas no miden horas ni certifican competencias.

## Edición y seguridad

El catálogo canónico está en `formacion/sistemas-operativos/planificacion/curriculo.json`. Los Markdown definen teoría y fichas; `content.py` añade apuntes y autoevaluaciones. `assets/navigation.js` genera el índice, orientación y búsqueda, sin otro catálogo manual. Recompilar actualiza lectura, presentación y asistente.

El parser escapa HTML crudo y limita protocolos; no ejecuta MDX ni instrucciones. La selección de documentos públicos es explícita. No incorporar expedientes, correos, secretos o exámenes reservados. La aplicación no añade analítica ni llamadas a modelos; el alojamiento puede conservar sus propios registros.

## Pruebas reproducibles

```sh
python3 -m unittest discover -s campus/tests -p 'test_*.py' -v
node --test campus/tests/*.test.mjs
python3 campus/build.py
python3 campus/check_release.py
python3 -m pip install playwright==1.55.0
python3 -m playwright install chromium
python3 campus/tests/browser.py
```

La dependencia Playwright solo pertenece al entorno de pruebas. CI conserva diagnósticos incluso con fallos y publica el artefacto `cloudflare-pages-ready` únicamente tras superar la aceptación. Consultar el resultado de la ejecución concreta: existir una prueba no significa haberla superado. Las pruebas web no acreditan ejecución de las 96 prácticas nativas.
