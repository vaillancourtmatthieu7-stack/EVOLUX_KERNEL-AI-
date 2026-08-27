from pathlib import Path

SANDBOX = Path.home() / "NanoAI" / "sandbox"
SANDBOX.mkdir(parents=True, exist_ok=True)

def workspace():
    return str(SANDBOX)
