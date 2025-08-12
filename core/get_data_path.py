from pathlib import Path
import os

def get_data_path(filename):
    base_path = Path(__file__).resolve().parent.parent  # now correctly points to WEN/
    return str(base_path / "data" / filename)