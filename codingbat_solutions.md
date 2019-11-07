# Codingbat Python Solutions
[codingbat.com](codingbat.com/python)

## List 2
### Count Evens
```
Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
```
Solution:
```python
def big_diff(nums):
    largest = nums[0]
    smallest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    
    return largest - smallest
```

### Big Diff
```
Given an array length 1 or more of ints, return the difference between the largest 
and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) 
functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

```
Solution:
```python
def big_diff(nums):
    largest = nums[0]
    smallest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    
    return largest - smallest
```

### Sum 67
```
Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

```
Solution:
```python
def sum67(nums):
    total = 0
    in_zone = False
    
    for num in nums:
        if num == 6:
            in_zone = True
        elif num == 7 and in_zone:
            in_zone = False
        elif not in_zone:
            total += num
    
    return total
```
