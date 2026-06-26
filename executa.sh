#!/bin/bash
set -euo pipefail

BASE_DIR="/Users/luizcarlosgrandisoli/Library/CloudStorage/OneDrive-Adobe/RFP_knowledge"
PYTHON_BIN="${PYTHON_BIN:-python3}"

cd "$BASE_DIR"

AEP_SCRIPT="$BASE_DIR/AEPRTCDP_crawler.py"
AJO_SCRIPT="$BASE_DIR/ajo_phase_1_crawler_rfp_flat.py"
CJA_SCRIPT="$BASE_DIR/cja_crawler_v4.py"
TARGET_SCRIPT="$BASE_DIR/target_crawler.py"
AGENTS_SCRIPT="$BASE_DIR/experience_cloud_ai_crawler.py"

AEP_OUT="$BASE_DIR/aep_guides"
AJO_OUT="$BASE_DIR/ajob2c_guides"
CJA_OUT="$BASE_DIR/cja_guides"
TARGET_OUT="$BASE_DIR/target_guides"
AGENTS_OUT="$BASE_DIR/agents"

CONSOLIDATED_DIR="$BASE_DIR/consolidados"

mkdir -p "$AEP_OUT"
mkdir -p "$AJO_OUT"
mkdir -p "$CJA_OUT"
mkdir -p "$TARGET_OUT"
mkdir -p "$AGENTS_OUT"
mkdir -p "$CONSOLIDATED_DIR"

echo "Limpando arquivos antigos..."

find "$AEP_OUT" -type f -name "*.md" -delete
find "$AJO_OUT" -type f -name "*.md" -delete
find "$CJA_OUT" -type f -name "*.md" -delete
find "$TARGET_OUT" -type f -name "*.md" -delete
find "$AGENTS_OUT" -type f -name "*.md" -delete
rm -f "$CONSOLIDATED_DIR"/*.md

echo "Executando AEP..."
"$PYTHON_BIN" "$AEP_SCRIPT" \
  --output-dir "$AEP_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Executando AJO..."
"$PYTHON_BIN" "$AJO_SCRIPT" \
  --output-dir "$AJO_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Executando CJA..."
"$PYTHON_BIN" "$CJA_SCRIPT" \
  --output-dir "$CJA_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Executando Target..."
"$PYTHON_BIN" "$TARGET_SCRIPT" \
  --output-dir "$TARGET_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Executando Experience Cloud AI Agents..."
"$PYTHON_BIN" "$AGENTS_SCRIPT" \
  --output-dir "$AGENTS_OUT" \
  --max-pages 5000 \
  --delay-s 0.5

echo "Gerando consolidados..."

cat "$AEP_OUT"/*.md > "$CONSOLIDATED_DIR/AEP_Consolidado.md"
cat "$AJO_OUT"/*.md > "$CONSOLIDATED_DIR/AJOB2C_Consolidado.md"
cat "$CJA_OUT"/*.md > "$CONSOLIDATED_DIR/CJA_Consolidado.md"
cat "$TARGET_OUT"/*.md > "$CONSOLIDATED_DIR/Target_Consolidado.md"
cat "$AGENTS_OUT"/*.md > "$CONSOLIDATED_DIR/Agents_Consolidado.md"

echo "Removendo arquivos markdown individuais..."

find "$AEP_OUT" -type f -name "*.md" -delete
find "$AJO_OUT" -type f -name "*.md" -delete
find "$CJA_OUT" -type f -name "*.md" -delete
find "$TARGET_OUT" -type f -name "*.md" -delete
find "$AGENTS_OUT" -type f -name "*.md" -delete

echo "Processo concluído."

echo "Processo concluído."