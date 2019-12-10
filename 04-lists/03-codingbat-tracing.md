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

###List-2 > has22
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
```
has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
```
Solution:
```python
def has22(nums):
  a=0
  for i in range(len(nums)):
    if nums[i]==2:
      a+=1
      if a==2:
        return True
    else:
      a=0
  if a<2:
    return False
```
