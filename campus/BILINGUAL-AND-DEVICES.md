# Campus bilingüe y continuidad / Bilingual campus and continuity

## Español

La edición 2.3 incorpora interfaz, módulos, fichas, autoevaluaciones, biblioteca y lectura continua en español e inglés. Cambiar idioma conserva la sección y utiliza los mismos identificadores de progreso. No duplica horas ni completa actividades. El original editorial permanece en español.

El inglés se prepara con traducción asistida, fuera del navegador del alumnado. Las correcciones explícitas de los títulos y todas las autoevaluaciones se conservan en `locales/en-overrides.json`. La compilación exige cobertura, rechaza traducciones ausentes u obsoletas y preserva bloques de comandos, URLs, identificadores y respuestas correctas. La cobertura estructural no sustituye una revisión lingüística independiente de cada frase. La lectura inglesa comunica esa limitación. No se afirma afiliación institucional.

### Continuar en otra pantalla

Abre el sitio publicado por HTTPS. En **Continuar en otro dispositivo**, pulsa **Crear enlace de continuación**. Comparte mediante el menú nativo, copia el enlace o abre Email, WhatsApp o Telegram. El campus no envía mensajes: eliges destinatario y confirmas en la aplicación. En el destino, revisa el resumen y selecciona **Combinar y continuar**.

Se trasladan lecturas, autoevaluaciones, favoritos, fases y punto de continuación. Se excluyen notas, datos personales, contraseñas, claves, cookies y credenciales. El receptor conserva sus notas y los avances se combinan. No es una sesión ni un acceso a una cuenta. Las marcas son autodeclaradas y cualquiera con el enlace puede importarlas. Caduca a los siete días según el reloj del cliente. Sin servidor no hay revocación, garantía de único uso ni sincronización automática.

Los datos están en el fragmento de URL, no en la consulta HTTP, y el navegador los retira de la barra al leerlos, antes de confirmar. **Mensajería, portapapeles y destinatarios pueden leer el enlace; no está cifrado.** No se usa acortador ni almacenamiento remoto. Compartir solo la lección no incorpora avances.

Para trasladar notas utiliza **Exportar progreso / Importar una copia**. Ese archivo sí incluye notas, no está cifrado y debe revisarse antes de compartir. La importación completa reemplaza el estado tras confirmación; el enlace combina marcas. Un dominio diferente tiene otro almacenamiento. En equipos compartidos, exporta y elimina el progreso al terminar.

En móvil o tableta puedes leer, presentar, revisar conceptos y tomar notas. Las prácticas administrativas deben ejecutarse en el sistema nativo indicado; leer instrucciones no acredita haberlas ejecutado.

### Email y OTP

No se presenta un formulario OTP ficticio ni envío de correo configurado. Cloudflare Access puede autenticar correos autorizados mediante OTP, pero **autenticar no sincroniza localStorage**. El progreso de cuenta requeriría API autenticada, verificación de JWT en servidor (firma, emisor, audiencia y caducidad), identidad estable, almacenamiento separado por alumno, control de concurrencia, retención, exportación y borrado. Un email enviado por el navegador no autoriza acceso.

Esta edición elige transferencia explícita sin cuenta para poder desplegar estáticamente sin recopilar identidades. No se ha activado Access ni contratado correo.

### Diseño y pruebas

Tema editorial independiente de blanco, gris carbón y rojo `#b5122d`, fuentes de sistema, foco visible y controles táctiles. Sin marcas institucionales. La matriz prevista cubre 320, 375, 390, 744, 768, 820, 1024 y 1366 CSS píxeles en Chromium/WebKit. Los resultados reales se registran en CI; una prueba de viewport no es una prueba física de cada iPad o aplicación de mensajería.

## English

Version 2.3 provides the interface, modules, lab briefs, self-assessments, library and continuous reader in Spanish and English. Language switching preserves the section and stable progress IDs. It neither adds hours nor completes tasks. Spanish remains the editorial source.

English is prepared with machine assistance, not translated on learners' devices. All module titles and self-assessments have explicit reviewed overrides in `locales/en-overrides.json`. The compiler rejects missing or stale translations and preserves command blocks, URLs, identifiers and correct-answer indices. Structural coverage is not independent linguistic proofreading of every sentence; the English reader states this limitation. No institutional affiliation is claimed.

### Continue on another device

Open the published HTTPS site, select **Continue on another device**, then **Create a continuation link**. Share through the native menu, copy the link, or open Email, WhatsApp or Telegram. You choose the recipient and send the message in that application. On the receiving device, preview the transfer and select **Combine and continue**.

The snapshot includes readings, self-assessments, bookmarks, lab stages and continuation location. It excludes notes, personal data, passwords, keys, cookies and credentials. Receiving notes are retained and completion flags are combined. It is not a login or account session. Anyone holding the link can import self-reported progress. The seven-day validity depends on the client clock; there is no server-enforced expiry, revocation, single use or automatic synchronization.

The snapshot uses the URL fragment rather than an HTTP query and is removed from the address bar once parsed, before approval. **Messaging apps, clipboard managers and recipients can read it; it is not encrypted.** No shortener or remote progress store is used. Sharing only a lesson excludes progress.

To transfer notes, use **Export progress / Import a backup**. This unencrypted file includes notes and needs review before sharing. Full import replaces state after confirmation; a continuation link combines flags. Different domains have separate storage. Export and clear progress when leaving a shared device.

Phones/tablets support reading, presentation, concept checks and notes. Run administration labs on the required native system; reading instructions is not evidence of execution.

### Email OTP

No pretend OTP form or configured mail delivery is provided. Cloudflare Access can authenticate approved email addresses, but authentication does not synchronize local storage. Account-backed progress needs a server-verified identity, JWT validation, authenticated API, per-learner storage, concurrency handling, retention, export and deletion. Never trust a client-supplied email as authorization. This release uses explicit account-free transfer for static deployment; Access and email have not been configured.

### Design and verification

An independent white, charcoal and red editorial theme uses system fonts, visible focus and touch controls, without institutional marks. The planned test matrix covers 320–1366 CSS-pixel viewports in Chromium and WebKit. CI records actual results; engine/viewport tests do not certify physical tablets or installed messaging apps.

## Primary references / Referencias primarias

- https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment
- https://developer.mozilla.org/en-US/docs/Web/API/Web_Share_API
- https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/
- https://developers.cloudflare.com/workers/ci-cd/builds/configuration/

Reviewed 2026-09-16. Provider deployment and authentication are reported separately from code and test availability.
