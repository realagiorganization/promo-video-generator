import os
from evaluate_site import write_next_steps_md

def test_write_next_steps_md(tmp_path):
    test_file = tmp_path / "test_nextsteps.md"
    write_next_steps_md(str(test_file))
    content = test_file.read_text(encoding="utf-8")
    assert "# Next Steps" in content
    assert "Playwright" in content

