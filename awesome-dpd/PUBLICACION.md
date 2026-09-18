# Publicación independiente en SmartKEA

## Estado

Contenido preparado dentro de `fundamentos-ciberseguridad/awesome-dpd`. Destino previsto: **smartkea-cyberinnovation/awesome-dpd**, público. **No creado ni transferido por esta integración**: el conector disponible no tiene acciones administrativas de creación/transferencia.

## Crear sin publicar datos accidentales

Desde una copia local revisada, generar el sitio y ejecutar las pruebas. Comprobar licencia, historial, documentos e imágenes antes de publicar; no trasladar `.git` del repositorio padre ni sus secretos/Actions.

```sh
# Ejecutar solo con GitHub CLI autenticada por el administrador.
# No pegar tokens aquí. Trabajar en una carpeta nueva y revisada.
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/render.py
# Desde la carpeta independiente del proyecto (no desde fundamentos):
git init -b main
git add README.md FUENTES.md CERTIFICACIONES.md ITINERARIO.md CASOS.md 90-DIAS.md   CONTRIBUTING.md SECURITY.md AVISO-LICENCIA.md PUBLICACION.md data plantillas tools tests site
# Revisar el índice antes de publicar:
git diff --cached --stat
git diff --cached --check
git commit -m "Initial reviewed DPD learning collection"
gh repo create smartkea-cyberinnovation/awesome-dpd --public --source=. --remote=origin --push
```

No ejecutar si la carpeta contiene un `.git` heredado. Si el destino ya existe, **detenerse y revisar**: no forzar push, borrar ni sobrescribir. La licencia queda pendiente de decisión del titular y no se anuncia automáticamente como open source.

## Transferir fundamentos

En GitHub: repositorio `WiktorNykiel/fundamentos-ciberseguridad` → Settings → General → Danger Zone → Transfer → `smartkea-cyberinnovation`. Confirmar derechos de creación en la organización, nombre libre, políticas y consecuencias. **Transferir** conserva la identidad del repositorio y su historial; copiar una carpeta o crear un fork no sustituye la transferencia.

Después: actualizar remotes, instalación GitHub App, permisos, reglas/protecciones, Actions, documentación y enlaces fuente. Verificar integración de Cloudflare y un despliegue de preview antes de producción. No afirmar que se migran automáticamente todos los servicios externos. Referencia oficial: https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository

## Checklist de aceptación

Destino real verificado; visibilidad pública comprobada; README y licencia revisados; ausencia de material sensible revisada; pruebas de contenido y navegador; enlaces entre repositorios actualizados; build reproducible; despliegue comprobado; nada de credenciales en historial. No borrar el repositorio original para simular una transferencia.
