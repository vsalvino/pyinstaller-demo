"""
Runs list_files on the current directory (".")
"""

from util import list_files


def main() -> None:
    path = "."
    files = list_files(path)
    for f in files:
        print(
            "d" if f.isdir else "f",
            f" {f.human_readable_bytes:<12}",
            f.path
        )


if __name__ == "__main__":
    main()
