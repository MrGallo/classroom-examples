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
### Big_Diff
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
```
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
```
Solutions: 
```python
largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
for num in nums:
    if num < smallest: 
        smallest = num 

diff = largest - smallest
return (diff)
```
### count_evens
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
```
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
```

Solutions: 

```python
def count_evens(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
        total += 1
     return total
```

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
