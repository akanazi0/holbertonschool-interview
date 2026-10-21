# Minimum Operations

## Description

This project contains a function that calculates the fewest operations needed to produce exactly `n` `H` characters in a text file.

The available operations are:

- **Copy All:** copy all characters currently in the file.
- **Paste:** paste the copied characters into the file.

## Requirements

- Python 3
- Files must start with `#!/usr/bin/python3`
- Code must follow PEP 8
- All files must be executable

## Usage

```python
#!/usr/bin/python3
minOperations = __import__('0-minoperations').minOperations

print(minOperations(4))  # 4
print(minOperations(12)) # 7
```

## Function

### `minOperations(n)`

Calculates the minimum number of operations required to produce exactly `n` copies of `H`.

- Returns the number of operations if `n` is reachable.
- Returns `0` if `n` is `0`, less than `0`, or otherwise unreachable.

## Files

- `0-minoperations.py`: contains the `minOperations` implementation
- `0-main.py`: example test file provided for the exercise
