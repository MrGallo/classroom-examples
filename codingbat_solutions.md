# Codingbat Python Solutions
[codingbat.com](codingbat.com/python)

**Table of Contents:**
- [List 2](#list-2)
  * [Count Evens](#count-evens)
  * [Big Diff](#big-diff)
  * [Centered Average](#centered-average)
  * [Sum 67](#sum-67)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## List 2
### Count Evens
Return the number of even ints in the given array.
Note: the `%` "mod" operator computes the remainder, e.g. `5 % 2` is `1`.
```
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
```
Solution:
```python
def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
```

### Big Diff
Given an array length 1 or more of ints, return the difference between the largest 
and smallest values in the array. Note: the built-in `min(v1, v2)` and `max(v1, v2)` 
functions return the smaller or larger of two values.
```
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

### Centered Average

Return the "centered" average of an array of ints, which we'll say is the mean 
average of the values, except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise 
for the largest value. Use int division to produce the final average. You may assume that 
the array is length 3 or more.
```
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
```
Solution:
```python
def centered_average(nums):
    total = 0
    largest = nums[0]
    smallest = nums[0]
    
    for num in nums:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        total += num
    
    # remove largest and smallest from total
    total = total - largest - smallest
    return total / (len(nums) - 2)
```

### Sum 67
Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.
```
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
