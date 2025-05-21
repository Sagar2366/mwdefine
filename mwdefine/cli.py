"""CLI for querying Merriam-Webster Collegiate Dictionary."""

import argparse
import os
import sys
from mwdefine.api import lookup
from mwdefine.formatter import pretty


def main():
    """
    Entry point for the mwdefine CLI.

    Parses command-line arguments, performs the API lookup,
    and prints the formatted definition or raw response.
    """
    parser = argparse.ArgumentParser(
        description="Query Merriam-Webster for a word definition."
    )
    parser.add_argument("word", help="Word to define")
    parser.add_argument(
        "--api-key",
        default=os.getenv("MW_API_KEY"),
        help="Merriam-Webster API key (or set MW_API_KEY)",
    )
    parser.add_argument("--raw", action="store_true", help="Show raw API response")
    args = parser.parse_args()

    if not args.api_key:
        print(
            "API key required. Use --api-key or MW_API_KEY env variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    entry = lookup(args.api_key, args.word)
    if args.raw:
        import json

        print(json.dumps(entry.__dict__ if entry else {}, indent=2))
        return

    print(pretty(entry))


if __name__ == "__main__":
    main()
