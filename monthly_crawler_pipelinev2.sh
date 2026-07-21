#!/bin/bash
set -euo pipefail

BASE_DIR="/Users/luizcarlosgrandisoli/Library/CloudStorage/OneDrive-Adobe/RFP_knowledge"

cd "$BASE_DIR" || exit 1

PYTHON_BIN="${PYTHON_BIN:-python3}"

AJO_SCRIPT="$BASE_DIR/ajo_phase_1_crawler_rfp_flat.py"
AJOB2B_SCRIPT="$BASE_DIR/ajob2b_crawler.py"
TARGET_SCRIPT="$BASE_DIR/target_crawler.py"

AJO_OUT="$BASE_DIR/ajob2c_guides"
AJOB2B_OUT="$BASE_DIR/ajob2b_guides"
TARGET_OUT="$BASE_DIR/target_guides"

AJO_CONSOLIDATED="$AJO_OUT/AJOB2C_Consolidado.md"
AJOB2B_CONSOLIDATED="$AJOB2B_OUT/AJOB2B_Consolidado.md"
TARGET_CONSOLIDATED="$TARGET_OUT/Target_Consolidado.md"

mkdir -p "$AJO_OUT"
mkdir -p "$AJOB2B_OUT"
mkdir -p "$TARGET_OUT"

# limpa todos os markdowns antigos
find "$AJO_OUT" -type f -name '*.md' -delete
find "$AJOB2B_OUT" -type f -name '*.md' -delete
find "$TARGET_OUT" -type f -name '*.md' -delete

echo "Executando crawler AJO..."
"$PYTHON_BIN" "$AJO_SCRIPT" \
  --output-dir "$AJO_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Executando crawler AJO B2B..."
"$PYTHON_BIN" "$AJOB2B_SCRIPT" \
  --output-dir "$AJOB2B_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Executando crawler Target..."
"$PYTHON_BIN" "$TARGET_SCRIPT" \
  --output-dir "$TARGET_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Concatenando arquivos..."

cat "$AJO_OUT"/*.md > "$AJO_CONSOLIDATED"

cat "$AJOB2B_OUT"/*.md > "$AJOB2B_CONSOLIDATED"

cat "$TARGET_OUT"/*.md > "$TARGET_CONSOLIDATED"

echo "Concluído."