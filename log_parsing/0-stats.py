#!/usr/bin/python3
"""Log parsing script."""

import sys
import re


def print_stats(total_size, status_counts):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


total_size = 0
status_counts = {}
valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0

pattern = re.compile(
    r'^(\d{1,3}\.){3}\d{1,3} - \[[^\]]+\] '
    r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.fullmatch(line.strip())

            if match:
                status_code = int(match.group(2))
                file_size = int(match.group(3))

                total_size += file_size

                if status_code in valid_codes:
                    status_counts[status_code] = (
                        status_counts.get(status_code, 0) + 1
                    )

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

    else:
        if line_count % 10 != 0:
            print_stats(total_size, status_counts)
