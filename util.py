"""
Utilities to list file info.
"""

from typing import List
import os


class MyFile:
    """
    Holds file info
    """
    def __init__(self, path: str, size_bytes: int):
        self.path = path
        self.size_bytes = size_bytes

    @property
    def human_readable_bytes(self) -> str:
        """
        Converts bytes to KB, MB, and GB.
        """
        bts = self.size_bytes
        kbs = round(bts / 1024, 2)
        mbs = round(kbs / 1024, 2)
        gbs = round(mbs / 1024, 2)
        if gbs > 1:
            return "{0} GB".format(gbs)
        if mbs > 1:
            return "{0} MB".format(mbs)
        if kbs > 1:
            return "{0} KB".format(kbs)
        return "{0} bytes".format(bts)


def list_files(directory: str) -> List[MyFile]:
    """
    Return list of files in the directory.
    """
    files = []
    for path in os.listdir(directory):
        if os.path.isfile(path):
            files.append(
                MyFile(
                    path,
                    os.path.getsize(path)
                )
            )
    return files
