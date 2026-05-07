#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

render_one() {
  local input_dir="$1"
  local pdf_name="$2"
  local source_file="$input_dir/guide-source.html"
  local output_file="$input_dir/$pdf_name"
  local file_url="file://$source_file"

  playwright pdf "$file_url" "$output_file" >/dev/null
}

render_one "$ROOT_DIR" "copilot-3d-ai-3d-model-generator-guide.pdf"
render_one "$ROOT_DIR/variants/vercel" "copilot-3d-ai-3d-model-generator-vercel-guide.pdf"
render_one "$ROOT_DIR/variants/github-pages" "copilot-3d-ai-3d-model-generator-github-pages-guide.pdf"
render_one "$ROOT_DIR/variants/pricing-guide" "copilot-3d-ai-3d-model-generator-pricing-guide.pdf"
render_one "$ROOT_DIR/variants/tool-page-guide" "copilot-3d-ai-3d-model-generator-tool-page-guide.pdf"
render_one "$ROOT_DIR/variants/showcase-guide" "copilot-3d-ai-3d-model-generator-showcase-guide.pdf"
render_one "$ROOT_DIR/variants/text-to-3d-guide" "copilot-3d-ai-3d-model-generator-text-to-3d-guide.pdf"
render_one "$ROOT_DIR/variants/image-to-3d-guide" "copilot-3d-ai-3d-model-generator-image-to-3d-guide.pdf"
