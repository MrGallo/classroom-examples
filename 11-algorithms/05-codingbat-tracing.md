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

### changePi
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
```
changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
```

Solutions:

```python
def changePi(word: str) -> str:
    """Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
    Args:
        word (str): The word to search in
    Returns:
        word (str) the new word with each instance of 'pi' replaced with '3.14'
    """

    if len(word) == 0 or len(word) == 1:
        return word
    
    if word[:2] == "pi":
        return "3.14" + word[:2] + changePi(word[2:])
    else:
        return changePi(word[1:])
```
