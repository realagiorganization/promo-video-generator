#!/usr/bin/env python3
"""Convert devplan.nextsteps.md into a Codex-friendly prompt."""
from pathlib import Path


def generate_codex_prompt(steps_path: str = "devplan.nextsteps.md", output_path: str = "codex_prompt.txt") -> None:
    """
    Convert devplan.nextsteps.md into a Codex-friendly prompt and write to output_path.
    Args:
        steps_path (str): Path to the markdown file with next steps.
        output_path (str): Path to write the Codex prompt.
    """
    steps_file = Path(steps_path)
    if not steps_file.exists():
        raise SystemExit(f"{steps_path} not found; run evaluate_site.py first")
    steps = steps_file.read_text(encoding="utf-8")
    prompt = f"Please implement the following next steps:\n\n{steps}\n"
    Path(output_path).write_text(prompt, encoding="utf-8")
    print(f"{output_path} written")

def main() -> None:
    """
    Generate a Codex prompt from the next steps markdown file.
    """
    generate_codex_prompt()


if __name__ == "__main__":
    main()
