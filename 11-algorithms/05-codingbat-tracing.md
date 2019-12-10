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

### count11
Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.
```
count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
```

Solutions:
```python
def count11(w: str, s: int = -1, e: int = -1, elevens: int = 0) -> int:
    if s == -1:
        s = 0
    if e == -1:
        e = 2
    
    try:
        if w[s:e] == '11':
            elevens += 1
            s += 2
            e += 2
        else:
            s += 1
            e += 1
        return count11(w, s, e, elevens)
    except:
        pass
    return elevens
```

