# src/cache.py
import os, json
RAW_DIR = "data/sample"
os.makedirs(RAW_DIR, exist_ok=True)

def save_snapshot(name, data):
    path = os.path.join(RAW_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path

def load_snapshot(name):
    path = os.path.join(RAW_DIR, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None
