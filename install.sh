#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME/NanoAI"
python -m venv .venv 2>/dev/null || true
source .venv/bin/activate
pip install -q flask requests
echo "NanoAI installé."
echo "Modèle: $HOME/models/nano.gguf"
echo "Lancement: ./launcher.sh"
