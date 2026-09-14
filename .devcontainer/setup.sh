#!/usr/bin/env bash
# Wird einmalig beim Erstellen des Codespaces (bzw. beim Prebuild) ausgeführt.
set -euo pipefail

echo "▶ PyTorch (nur CPU, ~200 MB statt 2,5 GB mit CUDA) installieren …"
pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

echo "▶ Restliche Pakete installieren …"
pip install --no-cache-dir -r requirements.txt

echo "▶ Jupyter-Kernel registrieren …"
python -m ipykernel install --user --name workshop --display-name "Python 3 (Workshop)"

echo "▶ Import-Test …"
python - <<'EOF'
import torch, sklearn, matplotlib
print("torch", torch.__version__, "| sklearn", sklearn.__version__, "| matplotlib", matplotlib.__version__)
EOF

echo "✔ Setup fertig."
