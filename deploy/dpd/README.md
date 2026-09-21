# Introducción DPD · Cloudflare

Target: `https://smartkea.com/introduccion-dpd/`.
Read `../../docs/codex/INTRODUCCION-DPD.md` before production work.

## Delivered, not deployed

39 Worker/packaging unit tests passed locally; the attached V2 mounted with 61
files and valid internal HTML links. Runtime workerd, Wrangler dry-run, zone
configuration and external HTTPS are not verified. This Git branch does NOT
replace PR #22's catalogue with V2: reconcile the attached V2 before release.

The overlay builds either `awesome-dpd/build.py` -> dist (V2) or
`awesome-dpd/tools/render.py` -> site (PR #22); it also supports build.py at the
root of an independent awesome-dpd repository. Output is isolated under
`deploy/dpd/public/introduccion-dpd`. No empty dist placeholder or campus mutation.

## Commands (from deploy/dpd)

```sh
npm test
python3 build_assets.py
# First-time connected toolchain setup: review actual release and audit results,
# then commit package.json and the resulting package-lock.json.
npm install --save-dev --save-exact wrangler@4
npm audit
npm ci
npm run dry-run
npm run dev
# Separate terminal; use the port printed by Wrangler:
node smoke.mjs http://localhost:8787
```

No fabricated lockfile is included. After actual browser acceptance and zone
preflight, `npm run preview` deploys a separate Worker without smartkea.com
routes. `npm run deploy` uses the production environment. Deployment requires
already authorised CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID. Prefer a
protected GitHub Actions job; the supplied checks workflow NEVER deploys.
Use one deployment controller, not concurrent Actions and Workers Builds.

## Mandatory preflight

Inventory existing routes, versions, proxied DNS, root redirects and baseline
HTTP behaviour in private operator storage. Do not take over smartkea.com/*,
change the apex Custom Domain, modify global WAF, or purge the zone.

Exact routes plus /introduccion-dpd/* do not match the no-slash URL with a query.
Review and enable the exact-path canonical Redirect Rule example (currently
DISABLED; not applied by Wrangler), or handle that case in the existing router.
The apex currently redirects to www: exclude only DPD where necessary and test
for loops. Do not silently change the requested canonical host to www.

The Worker applies security headers itself, only serves GET/HEAD and never
proxies the origin. Missing assets remain 404. LocalStorage namespaces are not
security boundaries between apps on the same origin; store no sensitive data.

After release: `EXPECTED_COMMIT=$(git rev-parse HEAD) node smoke.mjs https://smartkea.com`.
Record version/deployment IDs and compare the homepage and sibling routes with
the baseline. On failure restore only the captured DPD version/routes/rules.
A version upload or a successful command alone is not verified production.

References consulted 2026-09-20:
- https://developers.cloudflare.com/workers/static-assets/binding/
- https://developers.cloudflare.com/workers/configuration/routing/routes/
- https://developers.cloudflare.com/workers/static-assets/headers/
- https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/
- https://developers.openai.com/codex/cloud/environments/

Codex cloud setup secrets are removed before the agent phase. Never persist them
to files/.bashrc or ordinary variables to bypass that restriction. Use a protected
release job with its own secrets or an already authorised local CLI environment.
