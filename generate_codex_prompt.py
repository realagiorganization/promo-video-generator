#!/usr/bin/env python3
"""
Codex Prompt Generator
=====================

This module converts the development plan in devplan.nextsteps.md into a Codex-friendly prompt.
It reads the next steps, formats them as a prompt, and writes the result to codex_prompt.txt.

Intended for use after running evaluate_site.py, which generates devplan.nextsteps.md.
"""
from pathlib import Path


def generate_codex_prompt_from_devplan() -> None:
    """
    Read devplan.nextsteps.md and convert its contents into a Codex-friendly prompt.
    Writes the prompt to codex_prompt.txt.

    Raises:
        SystemExit: If devplan.nextsteps.md does not exist.

    Side Effects:
        Writes codex_prompt.txt to the current directory.
        Prints a confirmation message.
    """
    steps_path = Path("devplan.nextsteps.md")
    if not steps_path.exists():
        raise SystemExit("devplan.nextsteps.md not found; run evaluate_site.py first")
    steps = steps_path.read_text(encoding="utf-8")
    prompt = f"Please implement the following next steps:\n\n{steps}\n"
    Path("codex_prompt.txt").write_text(prompt, encoding="utf-8")
    print("codex_prompt.txt written")


if __name__ == "__main__":
    generate_codex_prompt_from_devplan()
