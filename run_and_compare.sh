#!/bin/bash
set -euo pipefail

# =============================================================================
# run_and_compare.sh
#   1. Renomeia os *_Consolidado.md atuais para *_Consolidado_old.md
#   2. Executa todos os crawlers .py
#   3. Concatena os .md de cada pasta gerando os novos consolidados
#   4. Compara cada *_Consolidado.md novo com o *_old.md e resume as diferencas
# =============================================================================

BASE_DIR="/Users/luizcarlosgrandisoli/Library/CloudStorage/OneDrive-Adobe/RFP_knowledge"
PYTHON_BIN="${PYTHON_BIN:-python3}"

cd "$BASE_DIR"

CONSOLIDATED_DIR="$BASE_DIR/consolidados"
mkdir -p "$CONSOLIDATED_DIR"

# Pasta de saida de cada crawler -> nome do consolidado correspondente
AEP_OUT="$BASE_DIR/aep_guides"
AJO_OUT="$BASE_DIR/ajob2c_guides"
CJA_OUT="$BASE_DIR/cja_guides"
TARGET_OUT="$BASE_DIR/target_guides"
AGENTS_OUT="$BASE_DIR/agents_guides"
WORKFRONT_OUT="$BASE_DIR/workfront_guides"

mkdir -p "$AEP_OUT" "$AJO_OUT" "$CJA_OUT" "$TARGET_OUT" "$AGENTS_OUT" "$WORKFRONT_OUT"

# -----------------------------------------------------------------------------
# 1. Renomeia os consolidados atuais para *_old.md (mantem como base de comparacao)
# -----------------------------------------------------------------------------
echo "==> Renomeando consolidados atuais para *_old.md ..."
shopt -s nullglob
# Remove _old.md antigos para nao acumular
rm -f "$CONSOLIDATED_DIR"/*_old.md
for f in "$CONSOLIDATED_DIR"/*_Consolidado.md; do
  mv -f "$f" "${f%.md}_old.md"
  echo "    $(basename "$f") -> $(basename "${f%.md}_old.md")"
done
shopt -u nullglob

# -----------------------------------------------------------------------------
# 2. Executa todos os crawlers .py
# -----------------------------------------------------------------------------
run_crawler() {
  local label="$1"; local script="$2"; local out_dir="$3"
  echo "==> Executando $label ($script) ..."
  # Limpa apenas os .md antigos da pasta de saida do crawler
  find "$out_dir" -maxdepth 1 -type f -name "*.md" -delete
  "$PYTHON_BIN" "$BASE_DIR/$script" \
    --output-dir "$out_dir" \
    --max-pages 5000 \
    --delay-s 0.5
}

run_crawler "AEP"      "AEPRTCDP_crawler.py"              "$AEP_OUT"
run_crawler "AJO B2C"  "ajo_phase_1_crawler_rfp_flat.py" "$AJO_OUT"
run_crawler "CJA"      "cja_crawler_v4.py"               "$CJA_OUT"
run_crawler "Target"   "target_crawler.py"               "$TARGET_OUT"
run_crawler "Agents"     "experience_cloud_ai_crawler.py"  "$AGENTS_OUT"
run_crawler "Workfront" "workfront_crawler_v4.py"         "$WORKFRONT_OUT"

# -----------------------------------------------------------------------------
# 3. Concatena os .md de cada pasta gerando os novos consolidados
# -----------------------------------------------------------------------------
concat_dir() {
  local dir="$1"; local out_file="$2"
  : > "$out_file"
  local found=0
  while IFS= read -r f; do
    found=1
    {
      echo ""
      echo "---"
      echo "# FILE: $(basename "$f")"
      echo "---"
      echo ""
      cat "$f"
      echo ""
    } >> "$out_file"
  done < <(find "$dir" -maxdepth 1 -type f -name "*.md" ! -name "README.md" | sort)
  if [ "$found" -eq 0 ]; then
    echo "    AVISO: nenhum .md encontrado em $dir"
  fi
  echo "    Gerado: $(basename "$out_file")"
}

echo "==> Gerando consolidados ..."
concat_dir "$AEP_OUT"    "$CONSOLIDATED_DIR/AEP_Consolidado.md"
concat_dir "$AGENTS_OUT" "$CONSOLIDATED_DIR/Agents_Consolidado.md"
concat_dir "$AJO_OUT"    "$CONSOLIDATED_DIR/AJOB2C_Consolidado.md"
concat_dir "$CJA_OUT"    "$CONSOLIDATED_DIR/CJA_Consolidado.md"
concat_dir "$TARGET_OUT"     "$CONSOLIDATED_DIR/Target_Consolidado.md"
concat_dir "$WORKFRONT_OUT" "$CONSOLIDATED_DIR/Workfront_Consolidado.md"

# -----------------------------------------------------------------------------
# 3b. Combina os README.md e os manifest.json de cada crawler em um unico
#     README.md e um unico manifest.json dentro da pasta consolidados.
#     (cada crawler gera README.md e manifest.json na sua pasta de saida)
# -----------------------------------------------------------------------------
# Lista "PASTA|RotuloDoConjunto" usada para o README e o manifest combinados
GUIDE_SETS=(
  "$AEP_OUT|AEP / RT-CDP"
  "$AGENTS_OUT|Experience Cloud AI Agents"
  "$AJO_OUT|AJO B2C"
  "$CJA_OUT|CJA"
  "$TARGET_OUT|Target"
  "$WORKFRONT_OUT|Workfront"
)

echo "==> Gerando README.md combinado em consolidados ..."
COMBINED_README="$CONSOLIDATED_DIR/README.md"
{
  echo "# RFP Knowledge - Indice consolidado dos guias"
  echo ""
  echo "Gerado em: $(date '+%Y-%m-%d %H:%M:%S')"
  echo ""
} > "$COMBINED_README"
for entry in "${GUIDE_SETS[@]}"; do
  dir="${entry%%|*}"; label="${entry#*|}"
  {
    echo ""
    echo "## $label"
    echo ""
  } >> "$COMBINED_README"
  if [ -f "$dir/README.md" ]; then
    cat "$dir/README.md" >> "$COMBINED_README"
  else
    echo "    AVISO: $dir/README.md nao encontrado"
    echo "_(README nao gerado para este conjunto)_" >> "$COMBINED_README"
  fi
  echo "" >> "$COMBINED_README"
done
echo "    Gerado: $(basename "$COMBINED_README")"

echo "==> Gerando manifest.json combinado em consolidados ..."
COMBINED_MANIFEST="$CONSOLIDATED_DIR/manifest.json"
"$PYTHON_BIN" - "$COMBINED_MANIFEST" "${GUIDE_SETS[@]}" <<'PY'
import json, sys
from pathlib import Path

out_path = Path(sys.argv[1])
entries = sys.argv[2:]
combined = []
for entry in entries:
    dir_str, label = entry.split("|", 1)
    mpath = Path(dir_str) / "manifest.json"
    if not mpath.exists():
        print(f"    AVISO: {mpath} nao encontrado")
        continue
    try:
        data = json.loads(mpath.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"    AVISO: falha ao ler {mpath}: {exc}")
        continue
    if isinstance(data, dict):
        data = [data]
    for item in data:
        if isinstance(item, dict):
            item = {"guide_set": label, **item}
        combined.append(item)

out_path.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"    Gerado: {out_path.name} ({len(combined)} entradas)")
PY

# -----------------------------------------------------------------------------
# 3c. Limpeza: remove os .md individuais e os manifest.json/README.md de cada
#     pasta apos consolidar (o conteudo ja foi movido para consolidados).
# -----------------------------------------------------------------------------
echo "==> Removendo arquivos individuais das pastas de origem ..."
for entry in "${GUIDE_SETS[@]}"; do
  dir="${entry%%|*}"
  find "$dir" -maxdepth 1 -type f -name "*.md" -delete
  rm -f "$dir/manifest.json"
done

# -----------------------------------------------------------------------------
# 4. Compara cada consolidado novo com o *_old.md e resume as diferencas
# -----------------------------------------------------------------------------
echo ""
echo "============================================================"
echo " RESUMO DAS DIFERENCAS (novo vs *_old.md)"
echo "============================================================"

summarize_diff() {
  local new_file="$1"
  local name; name="$(basename "$new_file")"
  local old_file="${new_file%.md}_old.md"

  echo ""
  echo "### $name"

  if [ ! -f "$old_file" ]; then
    local nl; nl=$(wc -l < "$new_file" | tr -d ' ')
    echo "    Sem versao anterior (NOVO). Linhas: $nl"
    return
  fi

  local old_lines new_lines old_bytes new_bytes added removed
  old_lines=$(wc -l < "$old_file" | tr -d ' ')
  new_lines=$(wc -l < "$new_file" | tr -d ' ')
  old_bytes=$(wc -c < "$old_file" | tr -d ' ')
  new_bytes=$(wc -c < "$new_file" | tr -d ' ')

  if cmp -s "$old_file" "$new_file"; then
    echo "    Sem alteracoes (identico). Linhas: $new_lines | Bytes: $new_bytes"
    return
  fi

  # Linhas adicionadas (>) e removidas (<) segundo o diff
  added=$(diff "$old_file" "$new_file" | grep -c '^> ' || true)
  removed=$(diff "$old_file" "$new_file" | grep -c '^< ' || true)

  echo "    Linhas: $old_lines -> $new_lines (delta $((new_lines - old_lines)))"
  echo "    Bytes : $old_bytes -> $new_bytes (delta $((new_bytes - old_bytes)))"
  echo "    Linhas adicionadas: $added | removidas: $removed"

  # Mudancas em nivel de arquivo (marcadores '# FILE:')
  local files_added files_removed
  files_added=$(diff "$old_file" "$new_file" | grep '^> # FILE:' | sed 's/^> # FILE: //' || true)
  files_removed=$(diff "$old_file" "$new_file" | grep '^< # FILE:' | sed 's/^< # FILE: //' || true)

  if [ -n "$files_added" ]; then
    echo "    Arquivos novos/alterados presentes no consolidado novo:"
    echo "$files_added" | sed 's/^/        + /'
  fi
  if [ -n "$files_removed" ]; then
    echo "    Arquivos que estavam no consolidado antigo e nao aparecem igual:"
    echo "$files_removed" | sed 's/^/        - /'
  fi
}

summarize_diff "$CONSOLIDATED_DIR/AEP_Consolidado.md"
summarize_diff "$CONSOLIDATED_DIR/Agents_Consolidado.md"
summarize_diff "$CONSOLIDATED_DIR/AJOB2C_Consolidado.md"
summarize_diff "$CONSOLIDATED_DIR/CJA_Consolidado.md"
summarize_diff "$CONSOLIDATED_DIR/Target_Consolidado.md"
summarize_diff "$CONSOLIDATED_DIR/Workfront_Consolidado.md"

echo ""
echo "============================================================"
echo " Processo concluido."
echo "============================================================"
