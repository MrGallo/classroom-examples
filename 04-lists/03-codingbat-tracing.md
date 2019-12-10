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

### makeEnds
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
```
make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
```
Solutions:

```python
def make_ends(nums: int) -> int:
  new_list = []
  new_list.append(nums[0]) 
  new_list.append(nums[-1]) 
  return new_list
```
End Example 
---

### middleWay 
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
```
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
```
Solutions:

```python 
def middle_way(a: int, b: int) -> int:
  new_list = []
  new_list.append(a[1]) 
  new_list.append(b[1])
  return new_list
```
End Example 
---
