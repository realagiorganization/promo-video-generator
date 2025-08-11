"""
Utility functions for file I/O and stub logging used by the promo video generator workflow.
"""
from pathlib import Path


def read_file(path: str) -> str:
    """Read and return the contents of a file as a string. Checks existence."""
    p = Path(path)
    # Raises FileNotFoundError if the file does not exist.

    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text(encoding="utf-8")


def write_file(path: str, content: str) -> None:
    """Write content to a file, ensuring a trailing newline."""
    # Writes the content to the specified path.

    # Ensures the file ends with a newline for markdown compatibility.

    # This is a stub for demonstration; in production, use proper logging configuration.

    Path(path).write_text(content.rstrip("\n") + "\n", encoding="utf-8")


def stub_print(message: str) -> None:
    """
    Log a stub message for demonstration purposes.
    Args:
        message (str): The message to log.
    """
    import logging
    logging.info(f"[stub] {message}")
