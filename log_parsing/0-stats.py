#!/usr/bin/python3
"""Parse HTTP logs and print statistics."""

import sys
import re


def print_stats(total_size, status_counts):
    """Print total file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))
