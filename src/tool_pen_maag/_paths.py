from pathlib import Path


def get_twin_assets_dir() -> Path:
    # twin_assets/ lives at the repo root, not inside the Python package
    return Path(__file__).parent.parent.parent / "twin_assets"
