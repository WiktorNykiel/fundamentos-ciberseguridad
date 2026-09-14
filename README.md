# Fundamentos de ciberseguridad

**Wiktor Nykiel · Sistemas operativos, terminal y administración segura · Español.**

[**Campus web: uso y despliegue**](campus/README.md) · [**Temario completo**](formacion/sistemas-operativos/README.md) · [Cloudflare Pages](campus/DEPLOY-CLOUDFLARE.md) · [Editar contenido](campus/EDICION.md) · [Pruebas del campus](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/workflows/campus.yml)

Comprender el sistema, practicar en un entorno propio, contrastar evidencias y explicar decisiones. El campus combina lectura, presentación, búsqueda, prácticas guiadas y progreso local. No ejecuta comandos ni requiere claves de IA.

| Bloque | Horas | Contenido principal |
|---|---:|---|
| [Fundamentos y método](formacion/sistemas-operativos/modulos/01-fundamentos.md) | 56 | Información, hardware, SO, procesos, memoria, terminal, laboratorio y Git. |
| [Linux y Bash](formacion/sistemas-operativos/modulos/02-linux.md) | 112 | Archivos, texto, usuarios, permisos, servicios, redes, copias y scripting. |
| [Windows, CMD, BAT y PowerShell](formacion/sistemas-operativos/modulos/03-windows.md) | 98 | Administración nativa, Registro, objetos, NTFS, servicios, eventos y recuperación. |
| [macOS, Darwin y zsh](formacion/sistemas-operativos/modulos/04-macos.md) | 56 | APFS, Finder/Terminal, preferencias, launchd, red y controles de plataforma. |
| [Operación y ciberseguridad](formacion/sistemas-operativos/modulos/05-operacion-seguridad.md) | 98 | Remoto, web/TLS, automatización, contenedores, logs, DFIR, IOCs y CTI. |
| [IA desde terminal](formacion/sistemas-operativos/modulos/06-ia.md) | 20 | Uso supervisado, privacidad, validación y revisión de scripts y datos sintéticos. |
| [Proyecto integrador](formacion/sistemas-operativos/CAPSTONE.md) | 40 | Construir, operar, proteger, investigar, recuperar y defender. |
| **Total** | **480** | **32 módulos · 168 h teoría · 312 h práctica · 96 fichas de laboratorio.** |

## Abrir localmente

```sh
python3 campus/build.py
python3 campus/serve.py --port 8788
```

Después abrir `http://127.0.0.1:8788`. El build genera también `campus/pages-ready.zip`. Para integración Git en Pages: raíz `campus`, comando `python3 build.py`, salida `dist`, rama `main`. No seleccionar el preset Next.js de la aplicación antigua.

## Qué está implementado

32 apuntes de apoyo y autoevaluaciones formativas, navegación por módulos/prerrequisitos, lectura continua sin JavaScript, presentación por secciones, biblioteca interna, guías por fases y exportación/importación de progreso. Las ocho guías prácticas ampliadas existentes se integran con sus fichas; no son 96 ejercicios nativos ya probados.

El seguimiento es autodeclarado y local, sin cuentas ni sincronización. Las pruebas de interfaz no acreditan ejecución de prácticas Windows/macOS o Docker/Swarm. El repositorio es público; publicar código no crea una URL de Cloudflare. Consultar [distribución](formacion/sistemas-operativos/PUBLICACION.md) y [documentación del campus](campus/README.md).

---

## Aplicación existente: documentación original

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
