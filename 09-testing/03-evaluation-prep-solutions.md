# Evaluation Prep Solutions
Watch the [video](https://youtu.be/LLlWQWhfvhk)
### `test_evaluation_prep.py`
```python
import evaluation_prep


def test_add():
    assert evaluation_prep.add(1, 1) == 2


def test_add_list():
    assert evaluation_prep.add_list([]) == 0
    assert evaluation_prep.add_list([1, 2, 3]) == 6


def test_count_occurances():
    initial_list = []
    expected = {}
    result = evaluation_prep.count_occurances(initial_list)
    assert result == expected

    initial_list = ["hello", "hello", "hello", "bye"]
    expected = {"hello": 3, "bye": 1}
    result = evaluation_prep.count_occurances(initial_list)
    assert result == expected

    initial_list = ["hello", "bye", "bye", "hello"]
    expected = {"hello": 2, "bye": 2}
    result = evaluation_prep.count_occurances(initial_list)
    assert result == expected

    
```

### `evaluation_prep.py`
```python
from typing import Dict, List


def add(a: int, b: int) -> int:
    """Adds two numbers.

    Args:
        a: An integer
        b: another integer
    Returns:
        The sum of the two integers
    """
    return a + b


def add_list(numbers: List[int]) -> int:
    """Adds up a list of integers.

    Args:
        numbers: List of integers.
    Returns:
        The sum of the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total


def count_occurances(words: List[str]) -> Dict:
    """Returns a dictionary of the occurances of each word.

    Args:
        words: a list of words.
    Returns:
        Dictionary with the key being the word,
        and the value being the number of
        occurances of that word in the list.

        e.g., 
        words = ["hello", "hello", "hello", "bye"]
        return {"hello": 3, "bye": 1}
    """
    occurances = {}
    for word in words:
        if word in occurances.keys():
            occurances[word] += 1
        else:
            occurances[word] = 1

    return occurances
```
