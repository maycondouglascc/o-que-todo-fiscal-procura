#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "$0")/.." && pwd)"
deploy_message="atualiza landing guia-nfe"
if [ "$#" -gt 0 ]; then deploy_message="$1"; fi

cd "$project_root"
git diff --check
node --check app.js
python3 growth-council/run_council.py verdict

npx --yes wrangler@latest deploy \
  --config wrangler.jsonc \
  --keep-vars \
  --message "$deploy_message"
