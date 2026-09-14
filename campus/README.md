# Campus web · Fundamentos de ciberseguridad

**Wiktor Nykiel · Versión 2.0.0 · Español · Interfaz clara.**

Campus estático construido desde el temario del repositorio. Conserva 32 módulos, 480 horas planificadas y 96 fichas de laboratorio. Añade 32 apuntes explicativos y 32 autoevaluaciones públicas. Integra las ocho guías R01–R08 disponibles y una biblioteca de referencias y lecciones. No sustituye el temario por diapositivas.

[Desplegar en Pages](DEPLOY-CLOUDFLARE.md) · [Editar contenidos](EDICION.md) · [Temario fuente](../formacion/sistemas-operativos/README.md) · [Comprobaciones en GitHub](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/workflows/campus.yml)

## Cinco recorridos conectados

**Explorar:** siete bloques, índice lateral desplegable, prerrequisitos enlazados y búsqueda de conceptos, comandos y prácticas. Las migas de navegación y anterior/siguiente mantienen la ubicación.

**Leer:** ancho de lectura, tablas desplazables, código copiable, índice interno, texto ampliable y cuaderno por módulo. La biblioteca abre referencias sin salir del campus. `lectura.html` proporciona el curso y sus referencias sin JavaScript, con índice e impresión.

**Presentar:** una diapositiva por sección, flechas, cierre con Escape y pantalla completa cuando el navegador la admite. Las secciones largas se desplazan; no se ocultan para caber. La presentación usa el mismo contenido que la lectura.

**Practicar:** preparar, ejecutar, comprobar, documentar y recuperar. Las guías ampliadas existentes aparecen dentro de la fase correspondiente. La plataforma seleccionada adapta las consultas de orientación, no convierte una práctica nativa en otra plataforma.

**Continuar:** lectura, autoevaluación, tres prácticas, favoritos y notas por módulo. Las cinco fases deben confirmarse antes de marcar una práctica terminada. Exportación/importación JSON validada y reinicio con confirmación.

## Inicio local

Desde la raíz de una copia completa del repositorio:

```sh
python3 campus/build.py
python3 campus/serve.py --port 8788
```

Abrir `http://127.0.0.1:8788`. No abrir el HTML mediante `file://`: la carga del catálogo necesita HTTP(S). Python 3.11+ para compilar; Node 22+ solo para pruebas JavaScript. Sin dependencias de producción ni descargas durante el build. El servidor de previsualización escucha únicamente en loopback y no es un backend de producción.

Se generan `campus/dist/`, `campus/pages-ready.zip`, `build-info.json` y `SHA256SUMS.txt`. El ZIP es el sitio compilado, no el código fuente completo. El kit incluido en descargas usa `oslab.py`; no mezclarlo con el paquete anterior `labkit.py`.

## Cloudflare Pages

| Ajuste | Valor |
|---|---|
| Repositorio | `WiktorNykiel/fundamentos-ciberseguridad` |
| Rama | `main` |
| Directorio raíz | `campus` |
| Framework | Ninguno |
| Comando | `python3 build.py` |
| Salida | `dist` |

El directorio `campus` evita instalar la aplicación Next.js de la raíz. El compilador lee `../formacion/sistemas-operativos/` del mismo checkout. Un commit o un ZIP no equivalen a un despliegue: la URL será la que devuelva Cloudflare al crear y publicar el proyecto. No se crea una cuenta, un dominio ni un recurso facturable desde este código.

## Fuente única

El catálogo canónico está en `formacion/sistemas-operativos/planificacion/curriculo.json`. Los Markdown de módulos y capstone definen las fichas; las guías R01–R08 amplían una selección. `content.py` añade apuntes y autoevaluaciones. Recompilar aplica los cambios a lectura, presentación y asistente.

El build comprueba IDs únicos y ordenados, prerrequisitos, cobertura de M01–M32, tres prácticas por módulo y 480/168 horas totales/teóricas. La biblioteca usa una lista explícita: no copia soluciones docentes, expedientes o cualquier archivo del repositorio. Esta selección no altera material que ya fuera público en el historial.

El parser admite títulos, párrafos, listas, tablas sencillas, enlaces, citas y código. Escapa HTML crudo y limita protocolos. No ejecuta MDX, plugins ni instrucciones dentro de los textos. Los documentos incluidos enlazan internamente; otras referencias conservan su fuente.

## Asistente: alcance real

El asistente es una guía editorial determinista: no es un modelo de IA ni una terminal remota. No abre SSH/WinRM/RDP, no instala software, no recibe secretos y no ejecuta órdenes. Copiar un comando no lo ejecuta. La comprobación de R01 compara las cantidades introducidas por el alumno con su dataset, no consulta su equipo.

Windows y macOS necesitan sus entornos nativos. Una ejecución administrada futura requiere un servicio separado con autenticación, autorización por práctica, aislamiento por sesión, límites, auditoría, expiración y aprobación humana. No debe implementarse con una shell abierta o claves dentro del frontend.

## Privacidad y progreso

160 hitos de seguimiento: lectura, autoevaluación y tres prácticas por módulo. No se miden horas reales ni se emiten certificaciones. Las marcas son autodeclaradas. El estado se guarda en `localStorage` del origen: cambiar navegador, dominio o dispositivo no lo sincroniza. Exportar antes de esos cambios.

Las notas y copias no están cifradas. No introducir información sensible. La importación limita tamaño, IDs, tipos, rutas y esquema. La aplicación no incorpora analítica propia ni llamadas a modelos; el alojamiento puede mantener sus propios registros de acceso. Las respuestas de autoevaluación son públicas y no sirven para un examen reservado.

## Verificación reproducible

```sh
python3 -m unittest discover -s campus/tests -p 'test_*.py' -v
npm --prefix campus test
python3 campus/build.py
# Dependencia exclusiva del entorno de pruebas:
python3 -m pip install playwright==1.55.0
python3 -m playwright install chromium
python3 campus/tests/browser.py
```

El workflow compila el curso real, ejecuta las pruebas y adjunta sitio, logs y capturas. Tiene permiso de lectura del repositorio y no despliega ni necesita secretos. La conclusión de cada ejecución se consulta en Actions: no se declara una validación por el mero hecho de existir un test. Las pruebas web no acreditan haber ejecutado las 96 prácticas nativas ni impartido la formación.
