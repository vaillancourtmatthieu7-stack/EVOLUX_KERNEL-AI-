#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME"
tar -czf "$HOME/NanoAI-backup.tar.gz" NanoAI \
  --exclude='NanoAI/.venv' \
  --exclude='NanoAI/server.log'
echo "Sauvegarde créée: $HOME/NanoAI-backup.tar.gz"
