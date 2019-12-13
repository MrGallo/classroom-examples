# Codingbat Solution Tracing
This is a collection of [Codingbat](http://codingbat.com) solutions that may or may not work. 
The idea is to trace the code to discover the errors or to determine if the solution is infact correct.

## Adding a post
Simply edit this document and add your code as shown below with the following rules:
1. Ensure your code is within triple backticks like below. 
2. Add [type annotations](https://docs.python.org/3/library/typing.html) for the function header so we know what type of data the function recieves and returns.
3. Ensure that the name of the function is under an appropriate `###` header.
4. Ensure that the problem's explanation text is above all the "solutions". 
5. Keep the problems in alpha order.

## Example:
### double
Create a function that will double the given integer.
```
double(5) -> 10
double(3) -> 6
double(0) -> 0
```
Solutions:

```python
def double(n: int) -> int:
    return n * 2
```

```python
def double(n: int) -> int:
    return n * 1
```

End example
---
### double_23
Given an int array, return true if the array contains 2 twice, or 3 twice. The array will be length 0, 1, or 2.

```
double_23([2, 2]) → true
double_23([3, 3]) → true
double_23([2, 3]) → false
```
Solutions:

```python
def double_23(list_1: list) -> bool:
    if len(list_1) == 0 or len(list_1) == 1:
        return False
    elif list_1[0] == 2 and list_1[1] == 2:
        return True
    elif list_1[0] == 3 and list_1[1] == 3:
        return True
    else:
        return False
```

### canBalance
Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.
```
canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true
```
Solutions:

```python
from typing import List
def canBalance(nums: List[int]) -> bool:
    length = len(nums)
    end = 1
    can_balance = False
    while end < length:
        sum_section1 = 0
        sum_section2 = 0
        section1 = nums[:end]
        section2 = nums[end:]

        for num_1 in section1:
            sum_section1 += num_1
        for num_2 in section2:
            sum_section2 += num_2

        if sum_section1 == sum_section2:
            can_balance = True
            break
        
        end += 1
        
    return can_balance
```

### either24
Given an array of ints, return true if the array contains a 2 next to a 2 or a 4 next to a 4, but not both.
```
either24([1, 2, 2]) → true
either24([4, 4, 1]) → true
either24([4, 4, 1, 2, 2]) → false
```
Solutions:

```python
from typing import List
def either24(nums: List[int]) -> bool:
    is2 = False
    is4 = False
    for index in range(len(nums) - 1):
        if nums[index] == 2 and nums[index + 1] == 2:
            is2 = True
        if nums[index] == 4 and nums[index + 1] == 4:
            is4 = True

    if is2 == True and is4 == False:
        return True
    elif is2 == False and is4 == True:
        return True
    else:
        return False
```

### isEverywhere
We'll say that a value is "everywhere" in an array if for every pair of adjacent elements in the array, at least one of the pair is that value. Return true if the given value is everywhere in the array.
```
isEverywhere([1, 2, 1, 3], 1) → true
isEverywhere([1, 2, 1, 3], 2) → false
isEverywhere([1, 2, 1, 3, 4], 1) → false
```
Solutions:

```python
from typing import List
def isEverywhere(nums: List[int], number: int) -> bool:
    everywhere = False
    for index in range(len(nums) - 1):
        if number == nums[index] or number == nums[index + 1]:
            everywhere = True
        else:
            return False
    
    return everywhere
```

### maxEnd3

Given an array of ints length 3, figure out which is larger, 
the first or last element in the array, and set all the other 
elements to be that value. Return the changed array.
```
max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
```
Solutions:

```python
def max_end3(nums):
  if nums[0] > nums[2]:
    nums[2] = nums[0]
    nums[1] = nums[0]
  elif nums[2] > nums[0]:
    nums[0] = nums[2]
    nums[1] = nums[2]
  else:
    nums[1] = nums[0]
  return nums
```
  
### no14
Given an array of ints, return true if it contains no 1's or it contains no 4's.
```
no14([1, 2, 3]) → true
no14([1, 2, 3, 4]) → false
no14([2, 3, 4]) → true
```
Solutions:

```python
from typing import List
def no14(nums: List[int]) -> bool:
    if 1 not in nums or 4 not in nums:
        return True

    return False
```
