#!/usr/bin/env bash
# Regenerates krova/_generated from openapi.json. Run from anywhere; needs uv.
# Refresh the spec first with: curl -fsSL https://krova.cloud/api/v1/openapi.json -o openapi.json
set -euo pipefail

GENERATOR_VERSION="0.28.4"

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

cat > "$tmp/config.yml" <<'YAML'
project_name_override: krova-generated
package_name_override: _generated
YAML

uvx --from "openapi-python-client==${GENERATOR_VERSION}" openapi-python-client generate \
  --path "$root/openapi.json" \
  --config "$tmp/config.yml" \
  --meta none \
  --output-path "$tmp/_generated" \
  --overwrite

rm -rf "$root/krova/_generated"
rm -rf "$tmp/_generated/.ruff_cache"
cp -R "$tmp/_generated" "$root/krova/_generated"
echo "Generated krova/_generated with openapi-python-client ${GENERATOR_VERSION}"
