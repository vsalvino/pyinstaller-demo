"""
Simple command line interface.
"""

from util import list_files


def main() -> None:
    path = "."
    files = list_files(path)
    for f in files:
        print(f"{f.path:<20}", f.human_readable_bytes)


if __name__ == "__main__":
    main()
