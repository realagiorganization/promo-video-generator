from pathlib import Path


def read_file(path: str) -> str:
    """Read and return the contents of a file as a string. Checks existence."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text(encoding="utf-8")


def write_file(path: str, content: str) -> None:
    """Write content to a file, ensuring a trailing newline."""
    Path(path).write_text(content.rstrip("\n") + "\n", encoding="utf-8")


def stub_print(message: str) -> None:
    """Log a stub message for demonstration purposes."""
    import logging
    logging.info(f"[stub] {message}")
