#!/data/data/com.termux/files/usr/bin/bash

cd "$HOME/NanoAI"

echo "=== NanoAI ==="

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

if ! pgrep -f "llama-server.*8765" >/dev/null 2>&1; then
    nohup "$HOME/llama.cpp/build/bin/llama-server" \
        -m "$HOME/models/nano.gguf" \
        -c 2048 \
        --host 127.0.0.1 \
        --port 8765 \
        > "$HOME/NanoAI/llama-server.log" 2>&1 &
    sleep 6
fi

echo "Serveur NanoAI :"
curl -s http://127.0.0.1:8765/v1/models

echo
echo "=== NanoAI PRET ==="
