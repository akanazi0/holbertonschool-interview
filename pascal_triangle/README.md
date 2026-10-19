# Pascal's Triangle

A Python implementation that returns Pascal's triangle as a list of lists of integers.

## Function

```python
def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size n."""
```

## Description

Pascal's triangle is constructed so that each number is the sum of the two numbers directly above it. The outer rows and columns contain `1`.

## Behavior

- If `n <= 0`, return an empty list.
- Otherwise, return the first `n` rows of Pascal's triangle.

## Example

```python
from pascal_triangle import pascal_triangle

print(pascal_triangle(5))
```

Output:

```python
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Requirements

- Python 3
- The result must be returned as a list of lists of integers
- The function must not use external libraries or return the triangle as a string

