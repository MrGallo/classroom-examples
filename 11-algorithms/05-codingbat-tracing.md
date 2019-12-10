# Codingbat Solution Tracing - Recursion-1
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

---**End example (YOUR CONTRIBUTIONS BELOW HERE)**---
```
count8(8) -> 1
count8(818) -> 2
count8(8818) -> 4
```
Solution 
```
def count8(g: int):
    count = 0
    prev_number = 0
    if (g == 0):
        return count
    if (g % 10 == 8):
        count = count + 1
        prev_number = count
    if(g == prev_number):
        count = count + 2
    
    return count + count8(g//10)
 ```
