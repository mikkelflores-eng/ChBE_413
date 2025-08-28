from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
def data_path(*parts):
    return ROOT / "hw" / "hw01" / "data" / Path(*parts)
