# Documentation Practice Solutions

For each function below, add **type annotations** and a **doc string**.

- [double_char](#double-char)
- [count_hi](#count-hi)
- [cat_dog](#cat-dog)
- [count_code](#count-code)
- [count_evens](#count-evens)
- [has_22](#has-22)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



## double_char
```python
def double_char(text: str) -> str:
    """Doubles each character in a given string.

    Args:
        text: Any string
    Returns:
        A string with every character doubled.
    """
    new_str = ""
    for char in text:
        new_str += char * 2
    
    return new_str```

## count_hi
```python
def count_hi(text: str) -> int:
    """Counts how many times 'hi' appears in a string.

    Args:
        text: Any string.
    Returns:
        The number of 'hi' substrings in the string.
    """
    count = 0
    for i in range(len(text) - 1):
        if text[i:i+2] == "hi":
            count += 1
    
    return count
```

## cat_dog
```python
def cat_dog(text: str) -> bool:
    """Determine if a string has an equal number of "cat" and "dog".

    Args:
        text: A string that may have the substrings "cat" and/or "dog".
    Returns:
        True if there is the same amount of "cat" and "dog" substrings.
    """
    diff = 0
    for i in range(len(text) - 2):
        slice = text[i:i+3]
        if slice == "cat": diff += 1
        elif slice == "dog": diff -= 1
    
    return diff == 0
```

## count_code
```python
def count_code(text: str) -> int:
    """Counts the occurances of "code", allowing a wildcard for the third letter.

    pslifpsolkdfj ;sldjf ;lskjdf ;lskjdf 
    sadf;lksj d;flkjs d;flkj asdf
    s;kldjf ;slkdfj ;ljdsa
    e.g., "cofe" will be counted.
    
    Args:
        text: Any string.
    Returns:
        The number of occurances of "code", with third letter wildcard.
    """
    count = 0
    for i in range(len(text) - 3):
        slice = text[i:i+4]
        if slice[0:2] == "co" and slice[-1] == "e":
            count += 1
    
    return count
```


## count_evens
```python
from typing import List

def count_evens(nums: List[int]) -> int:
    """Counts the number of even numbers in a list.

    Args:
        nums: A list of integers.
    Returns:
        How many integers in the list are even.
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
```

## has_22
```python
from typing import List


def has22(nums: List[int]) -> bool:
    """Checks if a list contains a 2 followed by a 2.

    Args:
        nums: A list of integers.
    Returns:
        True if the list contains a 2 followed by a 2.
    """
    for i, n in enumerate(nums):
        if i + 1 == len(nums):
            break
        if (n, nums[i+1]) == (2, 2):
            return True

    return False
```
