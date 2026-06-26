#!/bin/bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

AJO_SCRIPT="$BASE_DIR/ajo_phase_1_crawler_rfp_flat.py"
TARGET_SCRIPT="$BASE_DIR/target_crawler.py"

AJO_OUT="$BASE_DIR/ajob2c_guides"
TARGET_OUT="$BASE_DIR/target_guides"
AJO_CONSOLIDATED="$BASE_DIR/AJOB2C_Consolidado.md"
TARGET_CONSOLIDATED="$BASE_DIR/Target_Consolidado.md"

mkdir -p "$AJO_OUT" "$TARGET_OUT"

clean_markdown_dir() {
  local dir="$1"
  find "$dir" -type f -name '*.md' -delete
}

concatenate_markdown_dir() {
  local dir="$1"
  local output_file="$2"
  local title="$3"

  : > "$output_file"
  printf '# %s\n\n' "$title" >> "$output_file"

  local found=0
  while IFS= read -r -d '' file; do
    found=1
    rel_name="${file#$dir/}"
    {
      printf '\n\n---\n\n'
      printf '## %s\n\n' "$rel_name"
      cat "$file"
      printf '\n'
    } >> "$output_file"
  done < <(
    find "$dir" -type f -name '*.md' \
      ! -name 'README.md' \
      ! -name "$(basename "$output_file")" \
      -print | sort
  )

  if [ "$found" -eq 0 ]; then
    printf '\nNenhum arquivo .md encontrado em %s\n' "$dir" >> "$output_file"
  fi
}

clean_markdown_dir "$AJO_OUT"
clean_markdown_dir "$TARGET_OUT"

"$PYTHON_BIN" "$AJO_SCRIPT" --output-dir "$AJO_OUT" --max-pages 5000 --delay-s 0.5
"$PYTHON_BIN" "$TARGET_SCRIPT" --output-dir "$TARGET_OUT" --max-pages 5000 --delay-s 0.5

concatenate_markdown_dir "$AJO_OUT" "$AJO_CONSOLIDATED" "AJOB2C Consolidado"
concatenate_markdown_dir "$TARGET_OUT" "$TARGET_CONSOLIDATED" "Target Consolidado"
