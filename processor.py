# --------------------------------------------------------------------------------------------------
# File Name:       processor.py
# Created By:      Attila Liptak
# Creation Date:   October 18, 2024
# Description:     This file has the basic processing functionality for the project.
# Version:         0.0.1
# --------------------------------------------------------------------------------------------------
"""Processor providing txt to txt processing."""


from typing import TextIO
import sys

import exceptions


def main():
    """
    Executes the processing of the txt file.

    Parameters:
    file: File to be processed
    """
    if len(sys.argv) < 2:
        raise exceptions.NoFileSelectedError
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            process_file(f)
    except OSError as error:
        print(error)


def process_file(file: TextIO) -> None:
    """Processes the file, calling subprocesses during processing."""
    while True:
        line = file.readline()
        if not line:
            break


if __name__ == "__main__":
    main()
