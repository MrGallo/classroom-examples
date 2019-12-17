# Algorithms Section Goals

- [Linear Search](#linear-search)
    - Big-O and timeit
- Binary Search
    - Big-O and timeit
- Sort (Bubble, insertion, selection, pigeonhole, hashing)
    - Big-O and timeit
- [Recursion](#recursion)
- Merge Sort (recursion)
- Infinite recursion
- Binary Insert
- Memoization
- Tree traversal


### Linear Search
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

### Recursion
- Recursion: having a function call it self
- Base case: What is the final end-point of this algorithm?
- Recursive step: Call the function again. (algorithm not complete)

#### Base case
Try to figure out the end-point condition. i.e., `if n == 1: return 1`. This will stop the recursive calls and start the cascade back down the call stack.

#### Recursive step
Think about the function doing only their part and offloading the rest of the work to someone else. e.g., For `factorial(5)`, this function should say, "the answer is `5 x 4!`", thus, taking care of their own part, but passing off the rest to someone else (passing it to `factorial(4)`).

**Infinite Recursion**
```python
def hello():
    print("hello")
    hello()

hello()
```
outputs:
```
hello
hello
hello
.
.
. (ad infinitum)
```

**Counting down**
```python
def count_down(n):
    if n == 0:  # base case
        return
    
    # take care of this particular "n"
    print(n)

    # then pass off the responsibility
    # with a function call (recursive step)
    count_down(n-1)

count_down(5)
```
Outputs:
```
5
4
3
2
1
```

**Sum up to**
```python
def sum_up_to(n: int) -> int:
    if n == 1:  # base case
        return 1
    
    # recursive step
    return n + sum_up_to(n-1)


sum_up_to(4)  # result: 10
```
