import subprocess
from pathlib import Path

STOW_DIR = Path("~/.dotfiles").expanduser()
DEPENDENCIES = ["git", "stow"]


def ensure_dependencies():
    """Ensures that stow is installed"""
    for dep in DEPENDENCIES:
        if subprocess.call(["which", dep], stdout=subprocess.PIPE) != 0:
            raise EllipsisError(
                f"{dep} is required to run ellipses, please install {dep}."
            )


def ensure_dir():
    """Ensures that STOD_DIR exists"""
    if not STOW_DIR.exists():
        STOW_DIR.mkdir(parents=True)


def init():
    """Ensures that ellipses is configured"""
    ensure_dependencies()
    ensure_dir()
