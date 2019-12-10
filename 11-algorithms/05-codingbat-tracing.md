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

### changeXY
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
```
changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
```
Solutions:

```python
def changeXY(s: str) -> str:
    if len(s) == 0:
        return s
    
    if s[0] == 'x':
        return 'y' + changeXY(s[1:])
    
    return s[0] + changeXY(s[1:])
```

### count11
Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.
```
count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
```

Solutions:
```python
def count11(word: str) -> int:
    """Counts all of the '11's in the string
    Args:
        word (str): the word to find the '11's in
    Returns:
        (int) the numbers of '11's in word
    """
    
    # Base Case
    if len(word) == 0 or len(word) == 1:
        return 0
    
    # Recursive Step
    if word[:2] == "11":
        return 1 + count11(word[2:])
    else:
        return 0 + count11(word[1:])
```

