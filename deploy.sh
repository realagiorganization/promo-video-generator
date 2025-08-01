#!/bin/bash
set -euo pipefail

STACK_NAME=${1:-promo-video}

aws cloudformation deploy \
  --template-file cloudformation.yaml \
  --stack-name "$STACK_NAME" \
  --parameter-overrides EnvironmentName="$STACK_NAME"
