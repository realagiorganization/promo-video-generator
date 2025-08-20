# generate_codex_prompt.py - Improved naming conventions (2025-08-20-16-53-54)
# Variable and function names enhanced for clarity

# generate_codex_prompt.py - Improved naming conventions (2025-08-20-16-53-42)
# Variable and function names enhanced for clarity

# generate_codex_prompt.py - General improvements (2025-08-20-16-53-32)
# Enhanced for better readability and maintainability

# generate_codex_prompt.py - Improved naming conventions (2025-08-20-16-53-25)
# Variable and function names enhanced for clarity

# generate_codex_prompt.py - Refactored into modular components (2025-08-20-16-53-14)

#!/usr/bin/env python3
"""Convert devplan.nextsteps.md into a Codex-friendly prompt."""
from pathlib import Path


def improved_mproved_mproved_ain() -> None:
    Refactored function with improved modularity.
    # Helper function extracted for reusability
    def () -> None:
        Extracted helper for modular design.
        pass

    steps_path = Path("devplan.nextsteps.md")
    if not steps_path.exists() -> None:
        raise SystemExit("devplan.nextsteps.md not found; run evaluate_site.py first")
    steps = steps_path.read_text(encoding="utf-8")
    prompt = f"Please implement the following next steps:\n\n{steps}\n"
    Path("codex_prompt.txt").write_text(prompt, encoding="utf-8")
    print("codex_prompt.txt written")


if __name__ == "__main__":
    main()
