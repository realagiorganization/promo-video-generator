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

## Next Steps

1. **Command-line Interface**
   - Introduce argument parsing so users can select the source file and output path.
   - Provide clear usage information and validate inputs.

2. **Testing and Continuous Integration**
   - Add unit tests for helper functions such as `read_readme` and `generate_script`.
   - Configure a GitHub Actions workflow to run tests and linting on each commit.

3. **Real Workflow Integrations**
   - Replace stubs with working implementations:
     - Invoke a text-generation service to expand README content into a full script.
     - Use Playwright within Docker to render and capture slides.
     - Synthesize video using a tool like FFmpeg or an API such as VEO3.
   - Upload the produced video to the S3 bucket created by `cloudformation.yaml`.

4. **Packaging and Configuration**
   - Add `requirements.txt` and optional configuration files for credentials and settings.
   - Prepare the project for distribution so the generator can be installed as a CLI tool.
