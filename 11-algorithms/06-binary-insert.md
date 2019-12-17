Create a `binary_insert` function that will insert a number into a list and keep it sorted. See tests below:

```python
import random

from YOUR_FILE_NAME import binary_insert


def test_binary_insert():
    original = []
    expected = [6]
    assert binary_insert(original, 6) == expected

    original = [1, 3, 5]
    expected = [1, 3, 5, 6]
    assert binary_insert(original, 6) == expected

    original = [1, 3, 5]
    expected = [1, 3, 4, 5]
    assert binary_insert(original, 4) == expected

    original = [1, 3, 5]
    expected = [1, 3, 3, 5]
    assert binary_insert(original, 3) == expected

    original = [1, 3, 5, 7]
    expected = [1, 2, 3, 5, 7]
    assert binary_insert(original, 2) == expected

    original = [1, 3, 5, 7]
    expected = [0, 1, 3, 5, 7]
    assert binary_insert(original, 0) == expected

    original = [219, 450, 814, 897]
    expected = [219, 450, 563, 814, 897]
    assert binary_insert(original, 563) == expected


def test_acceptance():
    numbers = []
    for _ in range(1000):
        r = random.randrange(1000)
        numbers = binary_insert(numbers, r)
    
    expected = sorted(numbers)
    assert numbers == expected
```
