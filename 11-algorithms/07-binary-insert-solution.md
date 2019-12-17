# Binary Insert Solution
There are two versions. Make the tests pass however you can, then refactor.

## Binary Insert (Dirty)
```python
def binary_insert(numbers: List[int], value: int):
    if len(numbers) == 0:
        return [value]

    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == value:
            break
        elif numbers[mid] < value:
            start = mid + 1
        elif numbers[mid] > value:
            end = mid - 1

    if numbers[mid] >= value:
        index = mid
    elif numbers[mid] < value:
        index = mid+1

    numbers.insert(index, value)
    return numbers
```

## Binary Insert (Clean)
```python
def binary_insert(numbers: List[int], value: int) -> List[int]:
    index = 0
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] > value:
            end = mid - 1
            index = mid
        elif numbers[mid] <= value:
            start = mid + 1
            index = start

    numbers.insert(index, value)
    return numbers
```
