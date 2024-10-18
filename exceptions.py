# --------------------------------------------------------------------------------------------------
# File Name:       exceptions.py
# Created By:      Attila Liptak
# Creation Date:   October 18, 2024
# Description:     This file has the exceptions related to the processor.
# Version:         0.0.1
# --------------------------------------------------------------------------------------------------
"""File containing all Exceptions related to the processor."""


class NoFileSelectedError(Exception):
    """Exception for when a user doesn't provide a file to process"""

    def __str__(self):
        return "Please provide a file for the processor to process"
