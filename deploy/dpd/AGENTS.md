# DPD deployment scope

Read ../../docs/codex/INTRODUCCION-DPD.md and README.md before release work.
Never change the root smartkea.com route, its DNS, or the Fundamentos Worker.
Run npm test (Node built-ins and Python stdlib), then build_assets.py.
Wrangler and its lockfile must be resolved and reviewed in the connected build
environment; they were not available in the authoring container.
Use actual workerd/browser navigation before declaring deployment-ready.
Never write secrets to code, public assets, git history or logs.
