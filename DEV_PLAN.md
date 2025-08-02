# Development Plan: Promo Video Generator

This plan outlines steps to extend the repository so that it contains rudimentary source code for generating a promotional video based on the repository README.

1. **Define Workflow Script**
   - Implement a Python script (`promo_video_generator.py`) that demonstrates the intended workflow:
     - Read `README.md` for source text.
     - Create a placeholder script via a Codex-like stub.
     - Render slides (stub) and record them with a Playwright-like stub inside Docker.
     - Synthesize a video via a VEO3-like stub and output the video file name.
   - Keep all functions self-contained with no external dependencies or credentials.

2. **Documentation Updates**
   - Update `README.md` to mention the new script and explain that it is a non-functional placeholder illustrating the workflow.

3. **Quality Checks**
   - Run basic Python compilation to ensure no syntax errors.
   - Execute the script to show stubbed output.

Future improvements could integrate real API calls, containerisation, and automated testing once credentials and infrastructure are available.
