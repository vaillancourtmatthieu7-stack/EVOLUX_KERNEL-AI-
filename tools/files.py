from pathlib import Path

ROOT = Path.home() / "NanoAI"

def list_files(folder="projects"):
    path = ROOT / folder
    if not path.exists():
        return []
    return [str(p.relative_to(ROOT)) for p in path.rglob("*") if p.is_file()]
