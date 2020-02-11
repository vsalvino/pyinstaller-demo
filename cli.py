"""
Simple command line interface.
"""

import argparse
from util import list_files


def main() -> None:
    """
    Entrypoint into the command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Lists files in a directory."
    )

    parser.add_argument(
        "path",
        type=str,
        help="The path to show files in."
    )

    # Parse and process commands

    args = parser.parse_args()

    if args.path:

        path = args.path
        files = list_files(path)
        for f in files:
            print(
                "d" if f.isdir else "f",
                f" {f.human_readable_bytes:<12}",
                f.path
            )


if __name__ == "__main__":
    main()
