#!/usr/bin/python3
"""Module that calculates the minimum number of operations

to get n H characters.
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in

    exactly n 'H' characters in the file.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations, or 0 if n <= 1.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
