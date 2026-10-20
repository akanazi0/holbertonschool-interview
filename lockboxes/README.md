# Lockboxes

## Description

This project implements an algorithm that determines whether all boxes in a list can be opened.

Each box contains a list of keys, and each key is represented by an integer corresponding to the index of a box. A box is opened when a key for it is found. A box may contain keys for itself or for boxes that have not yet been opened.

The first box (`boxes[0]`) is assumed to be unlocked at the start.

## Requirements

- The input is a list of lists.
- A key is considered valid only if it matches an existing box index.
- The method must return `True` if all boxes can be opened, otherwise it must return `False`.
- Keys can be opened only after visiting the box that contains them.
- Boxes should not be opened more than once.

## Usage

```python
from lockboxes import canUnlockAll

boxes = [
    [1],
    [2],
    [3],
    [],
]

print(canUnlockAll(boxes))  # True
```

## Algorithm

The algorithm uses a set of opened boxes and a list of boxes waiting to be checked:

1. Mark box `0` as opened.
2. Add box `0` to the list of boxes to visit.
3. Visit each box, collect its keys, and open any valid box that has not been opened yet.
4. Return `True` only when the number of opened boxes equals the total number of boxes.
