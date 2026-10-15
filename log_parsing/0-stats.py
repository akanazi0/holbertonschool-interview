#!/usr/bin/python3
"""Module that reads stdin line by line and computes log metrics."""
import sys


def print_stats(total_size, status_codes):
    """Prints the accumulated log statistics.

    Args:
        total_size (int): The sum of all file sizes processed so far.
        status_codes (dict): Dictionary mapping status codes to their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Processes lines from stdin and handles printing metrics."""
    total_size = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_codes = {code: 0 for code in valid_codes}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Process file size
            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Process status code
            try:
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except IndexError:
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Print stats when stdin ends normally
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
