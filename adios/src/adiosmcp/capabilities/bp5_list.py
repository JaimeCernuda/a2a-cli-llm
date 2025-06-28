
import glob
from pathlib import Path

def list_bp5(directory: str = "data") -> list[str]:
    """
    Return a list of all .bp file paths under the specified directory.
    Raises FileNotFoundError if the directory doesn't exist.
    """
    base = Path(directory)
    if not base.exists():
        raise FileNotFoundError(f"Directory '{directory}' not found")

    # Use glob to match *.bp
    return list(base.glob("*.bp"))