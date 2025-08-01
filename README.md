# Promo Video Generator

This repository contains a minimal example for generating a promotional video.

Contents:
- `cloudformation.yaml` – defines AWS infrastructure for storing generated videos.
- `deploy.sh` – script that deploys the CloudFormation stack.
- `.microagent/.openhands/microagent/promo-video-agent.md` – instructions for requesting credits and creating the promo video using Codex, VEO3, Docker and Playwright.

No keys or personal data are present in this repository.

## Deploying the infrastructure

Run `./deploy.sh` to create the S3 bucket defined in `cloudformation.yaml`. An optional stack name may be supplied; it will also be used as the environment name:

```bash
./deploy.sh my-stack-name
```
