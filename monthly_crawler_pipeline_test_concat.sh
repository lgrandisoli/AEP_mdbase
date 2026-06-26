#!/bin/bash
set -euo pipefail

BASE_DIR="/Users/luizcarlosgrandisoli/Library/CloudStorage/OneDrive-Adobe/RFP_knowledge"
AJOB_DIR="$BASE_DIR/ajob2c_guides"
TARGET_DIR="$BASE_DIR/target_guides"

mkdir -p "$AJOB_DIR" "$TARGET_DIR"
cd "$BASE_DIR"

# Limpa somente os .md antigos, sem mexer em outros arquivos
find "$AJOB_DIR" -maxdepth 1 -type f -name '*.md' -delete
find "$TARGET_DIR" -maxdepth 1 -type f -name '*.md' -delete

# Cria arquivos de teste para validar o concat
cat > "$AJOB_DIR/01_teste.md" <<'EOF'
# AJOB2C - Teste 1

Conteudo de teste 1.
EOF

cat > "$AJOB_DIR/02_teste.md" <<'EOF'
# AJOB2C - Teste 2

Conteudo de teste 2.
EOF

cat > "$TARGET_DIR/01_teste.md" <<'EOF'
# Target - Teste 1

Conteudo de teste 1.
EOF

cat > "$TARGET_DIR/02_teste.md" <<'EOF'
# Target - Teste 2

Conteudo de teste 2.
EOF

concat_dir() {
  local dir="$1"
  local out_file="$2"
  : > "$out_file"
  for f in $(find "$dir" -maxdepth 1 -type f -name '*.md' ! -name 'AJOB2C_Consolidado.md' ! -name 'Target_Consolidado.md' | sort); do
    {
      echo ""
      echo "---"
      echo "# FILE: $(basename "$f")"
      echo "---"
      echo ""
      cat "$f"
      echo ""
    } >> "$out_file"
  done
}

concat_dir "$AJOB_DIR" "$AJOB_DIR/AJOB2C_Consolidado.md"
concat_dir "$TARGET_DIR" "$TARGET_DIR/Target_Consolidado.md"

echo "OK"
echo "$AJOB_DIR/AJOB2C_Consolidado.md"
echo "$TARGET_DIR/Target_Consolidado.md"
