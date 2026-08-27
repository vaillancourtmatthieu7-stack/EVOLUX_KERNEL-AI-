from pathlib import Path
import json

ROOT = Path.home() / "NanoAI"
PROJECTS = ROOT / "projects"

def create_project(name):
    path = PROJECTS / name
    path.mkdir(parents=True, exist_ok=True)
    return str(path)

def list_projects():
    return [p.name for p in PROJECTS.iterdir() if p.is_dir()]
