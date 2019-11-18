# Algorithms Section Goals

- [Linear Search](#linear-search)
    - Big-O and timeit
- Binary Search
    - Big-O and timeit
- Sort (Bubble, insertion, selection, pigeonhole, hashing)
    - Big-O and timeit
- Recursion
- Merge Sort (recursion)
- Infinite recursion
- Memoization


# Linear Search
```python
from typing import List

def linear_search(target: int, numbers: List[int]) -> int:
    """Search for a target value.

    Args:
        target: The int to search for.
        numbers: List of numbers.
    Returns:
        Index location of the found target number. -1 if not found.
    """
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1


def test_linear_search():
    assert linear_search(5, []) == -1
    assert linear_search(5, [5]) == 0
    assert linear_search(5, [1, 2, 3, 4, 5]) == 4
    assert linear_search(5, [2, 5, 2]) == 1
    assert linear_search(5, [6, 5, 5]) == 1
```