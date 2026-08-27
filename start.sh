#!/data/data/com.termux/files/usr/bin/bash
cd "$(dirname "$0")"
PORT=$(python -c 'import socket;s=socket.socket();s.bind(("127.0.0.1",0));print(s.getsockname()[1]);s.close()')
echo "🧠 NanoAI → http://127.0.0.1:$PORT/ui/"
python -m http.server "$PORT" --bind 127.0.0.1
