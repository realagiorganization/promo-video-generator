# Promo Video Generator

This repository contains a minimal example for generating a promotional video.

## Contents
- `cloudformation.yaml` – defines AWS infrastructure for storing generated videos.
- `.microagent/.openhands/microagent/promo-video-agent.md` – instructions for requesting credits and creating the promo video using Codex, VEO3, Docker and Playwright.
- `promo_video_generator.py` – placeholder Python script illustrating how the workflow could be orchestrated.

No keys or personal data are present in this repository.

## Prerequisites
To reproduce the workflow you'll need the following tools installed:
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) for deploying the stack.
- [Docker](https://docs.docker.com/get-docker/) to run the containerised video generation process.
- Optional tooling such as Node.js or Python depending on how you choose to orchestrate the workflow.

## Deploying the infrastructure
Create the S3 bucket and other resources with AWS CloudFormation:

```bash
aws cloudformation deploy \
  --stack-name promo-video-stack \
  --template-file cloudformation.yaml \
  --parameter-overrides EnvironmentName=myenv \
  --capabilities CAPABILITY_NAMED_IAM
```

Replace `myenv` with the desired value for the `EnvironmentName` parameter. The parameter is used as a prefix for all created resources.

## About the microagent document
The microagent markdown file describes a conceptual workflow for generating the promo video. It outlines how tools like VEO3, Docker and Playwright could be used together but does not contain executable code.

## Placeholder promo video script
`promo_video_generator.py` demonstrates the high-level steps without invoking external services:

```bash
python promo_video_generator.py
```

The script reads `README.md`, simulates script generation, stub slide rendering, and stub video synthesis. It is intended for illustration only and does not produce an actual video.
