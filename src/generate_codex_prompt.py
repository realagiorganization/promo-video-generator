#!/usr/bin/env python3
"""
Script to convert devplan.nextsteps.md into a Codex-friendly prompt for further automation.
"""

import argparse
import logging
from utils import read_file, write_file
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Convert devplan.nextsteps.md to Codex prompt.")
    parser.add_argument('--input', default="devplan.nextsteps.md", help="Input markdown file")
    parser.add_argument('--output', default="codex_prompt.txt", help="Output prompt file")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    steps_path = Path(args.input)
    if not steps_path.exists():
        raise SystemExit(f"{args.input} not found; run evaluate_site.py first")
    steps = read_file(args.input)
    prompt = f"Please implement the following next steps:\n\n{steps}\n"
    write_file(args.output, prompt)
    logging.info(f"{args.output} written")

if __name__ == "__main__":
    main()
