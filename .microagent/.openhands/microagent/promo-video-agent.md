# Promo Video Microagent

This microagent is responsible for coordinating the creation of a promotional video using the minimal content from this repository.

## Purpose

Request approximately **$3000** in credits to generate a promotional video using VEO3. The video is produced from the text found in `README.md` and scripted by Codex. It features two founders talking while demonstrating the repository website via a Docker-hosted slide deck recorded with Playwright.

## Workflow

1. Read `README.md` to gather source text.
2. Use Codex to expand the README into a script involving two founders discussing the project.
3. With the script, call VEO3 to synthesize a video.
4. Render slides via a lightweight website and record the presentation using Playwright in Docker.
5. Upload the final video to the cloud infrastructure defined by `cloudformation.yaml`.

Ensure no personal data or credentials are introduced during the process.
