# Cybersecurity foundations · Start here

Independent course by Wiktor Nykiel. A light, responsive campus with Spanish/English reading, presentations, guided labs and learner-controlled progress. It uses the existing curriculum: 32 modules, 96 lab briefs and 480 planned hours. A translation does not add or certify learning hours.

## Study on the device you have

Open the published HTTPS site and select English. Use **Start here** for orientation and **Full index** to filter modules by block, status or search terms. Every module links to its prerequisites, theory, three labs and formative self-assessment. Prerequisites guide you without locking the content.

Read the theory and explain the mechanism before running a command. Use presentation mode when teaching or reviewing together. On a phone or tablet, you can read, answer concept checks, take notes and follow instructions. Administrative commands must be executed manually in the specified native lab environment. A browser button does not execute a shell command or provide evidence of success.

Each guided lab has five stages: identify the environment, execute within scope, verify positive and negative cases, document evidence, and recover. Confirm only what you actually completed. A full module combines reading, the three labs and its self-assessment.

## Continue on another device

Choose **Continue on another device → Create a continuation link**. Send the link to yourself using the system share menu or the Email, WhatsApp or Telegram links. Nothing is sent automatically. The receiving device previews the snapshot; **Combine and continue** adds the imported completion flags without deleting existing notes.

The link is not a login. It excludes notes and credentials, is readable by anyone holding it and uses a client-checked seven-day expiry. It is not live synchronization or certification. For notes, use the separate full JSON backup, which is unencrypted and replaces state only after confirmation. See [Bilingual campus and device continuity](BILINGUAL-AND-DEVICES.md).

## Deploy the static campus

Cloudflare Pages Git integration:

| Setting | Value |
|---|---|
| Production branch | `main` |
| Root directory | `campus` |
| Framework | None |
| Build | `python3 build.py && python3 check_release.py` |
| Output | `dist` |
| Environment | `SKIP_DEPENDENCY_INSTALL=1`, `PYTHON_VERSION=3.13` |

For a Workers project, keep the repository root and use `python3 campus/cloudflare.py deploy`; use `python3 campus/cloudflare.py preview` for preview versions. These wrappers compile and validate assets before calling the pinned Wrangler. Do not deploy the unrelated legacy Next.js application or run an automatic OpenNext migration.

The accepted `pages-ready.zip` contains the website at its root and may be uploaded to Pages Direct Upload. A Direct Upload project cannot later be converted into a Git-integrated project; decide before creating it. See [deployment and diagnostics](DEPLOY-CLOUDFLARE.md).

## Language and verification

The interface and reviewed assessment wording are explicit translations. The full English catalogue uses versioned machine-assisted prose with editorial overrides. The compiler rejects missing/stale segments and checks identifiers, links, command blocks and answer indices. That coverage is not independent proofreading of every sentence; compare the Spanish source when wording is ambiguous.

The production build needs Python's standard library, not a model or an AI API key. No inference runs on learner devices. Tests include English/Spanish navigation and progress, additive transfer and responsive Chromium/WebKit viewports. CI logs show which tests actually passed; configuration files alone are not proof of deployment. No Cloudflare account, mail service or OTP provider is provisioned by this repository.
