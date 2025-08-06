import os
from generate_codex_prompt import generate_codex_prompt

def test_generate_codex_prompt(tmp_path):
    steps_file = tmp_path / "steps.md"
    output_file = tmp_path / "prompt.txt"
    steps_file.write_text("# Steps\n- [ ] Do something\n", encoding="utf-8")
    generate_codex_prompt(str(steps_file), str(output_file))
    content = output_file.read_text(encoding="utf-8")
    assert "Please implement the following next steps" in content
    assert "Do something" in content

