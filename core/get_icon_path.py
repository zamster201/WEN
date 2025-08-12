from pathlib import Path

def get_icon_path(filename: str) -> str:
    """
    Returns the absolute path to an icon file in wen/resources/icons.
    """
    return str(Path(__file__).resolve().parent.parent.parent / "resources" / "icons" / filename)