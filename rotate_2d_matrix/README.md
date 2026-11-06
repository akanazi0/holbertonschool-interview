# Rotate 2D Matrix

This project contains a Python algorithm to rotate an $n \times n$ 2D matrix 90 degrees clockwise **in-place**.

## Requirements

- Python 3.8+
- Code should follow `pycodestyle` (PEP 8) standards.
- All files must be executable.

## File Descriptions

| File | Description |
| --- | --- |
| `0-rotate_2d_matrix.py` | Function `rotate_2d_matrix(matrix)` that rotates an $n \times n$ matrix 90 degrees clockwise in-place. |
| `main_0.py` | Main file for testing the function. |

## Usage

You can test the function using the following script:

```python
#!/usr/bin/python3
"""
Test - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
