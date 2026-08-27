#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME/NanoAI"
source .venv/bin/activate 2>/dev/null || true
MODEL="$HOME/models/nano.gguf"
SERVER="$HOME/llama.cpp/build/bin/llama-server"
if ! curl -s http://127.0.0.1:8765/v1/models >/dev/null 2>&1; then
  "$SERVER" -m "$MODEL" -c 2048 --host 127.0.0.1 --port 8765 > "$HOME/NanoAI/server.log" 2>&1 &
  sleep 8
fi
python app.py
