import os
from promo_video_generator import read_readme, generate_script, render_slides, synthesize_video

def test_read_readme():
    content = read_readme("README.md")
    assert isinstance(content, str)
    assert len(content) > 0

def test_generate_script():
    script = generate_script("Hello world!")
    assert script.startswith("Script derived from README:")

def test_render_slides():
    slides = render_slides("Some script")
    assert slides == "slides"

def test_synthesize_video():
    video = synthesize_video("script", "slides")
    assert video == "promo_video.mp4"

