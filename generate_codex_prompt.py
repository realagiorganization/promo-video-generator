# generate_codex_prompt.py - Enhanced by OpenHands AI (2025-08-20-16-26-13)

# generate_codex_prompt.py - Enhanced by OpenHands AI (2025-08-20-16-26-10)

# generate_codex_prompt.py - Enhanced by OpenHands AI (2025-08-20-16-26-06)

# generate_codex_prompt.py - Enhanced by OpenHands AI (2025-08-20-16-26-03)

#!/usr/bin/env python3
"""Convert devplan.nextsteps.md into a Codex-friendly prompt."""
from pathlib import Path


def main() -> None:
    steps_path = Path("devplan.nextsteps.md")
    if not steps_path.exists():
        raise SystemExit("devplan.nextsteps.md not found; run evaluate_site.py first")
    steps = steps_path.read_text(encoding="utf-8")
    prompt = f"Please implement the following next steps:\n\n{steps}\n"
    Path("codex_prompt.txt").write_text(prompt, encoding="utf-8")
    print("codex_prompt.txt written")


if __name__ == "__main__":
    main()
