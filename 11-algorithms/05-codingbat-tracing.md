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

### allStar
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
```
allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
```
Solutions:
```python
def allStar(str_: str) -> str:
    if len(str_) <= 1:
        return str_
    return str_[0] + "*" + allStar(str_[1:])
```
### array11
Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
```
array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0
```
Solutions:
```python
def array11(arr: List[int], x: int) -> int:
    if x == len(arr):
        return 0
    return int(arr[x] == 11) + array11(arr, x+1)
```

### array220
Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
```
array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
```
Solutions:

```python
def array220(arr: List[int], x: int) -> bool:
    if x+1 >= len(arr):
        return 0
    return arr[x]*10 == arr[x+1] or array220(arr, x+1)
```

### array6
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
```
array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
```
Solutions:

```python
def array6(arr: List[int], x: int) -> bool:
    if x == len(arr):
        return 0
    return arr[x] == 6 or array6(arr, x+1)
```

### bunnyEars
We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
```
bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
```
Solutions:

```python
def bunnyEars(x: int) -> int:
    if x == 0:
        return 0
    return 2 + bunnyEars(x-1)
```

### bunnyEars2
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
```
bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
```
Solutions:

```python
def bunnyEars2(x: int) -> int:
    if x == 0:
        return 0
    return (x % 2 == 0) + 2 + bunnyEars2(x-1)
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
def changePi(str_: str) -> str:
    if len(str_) == 0:
        return ""
    if str_[:2] == "pi":
        return "3.14" + changePi(str_[2:])
    return str_[0] + changePi(str_[1:])
```

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
def count11(str_: str) -> int:
    if len(str_) <= 1:
        return 0
    if str_[:2] == "11": 
        return 1 + count11(str_[2:])
    return count11(str_[1:])
```

### count7
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
```
count7(717) → 2
count7(7) → 1
count7(123) → 0
```
Solutions:
```python
def count7(x: int) -> int:
    if x == 0:
        return 0
    return (x % 10 == 7) + count7(x//10)
```

### count8
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
```
count8(8) → 1
count8(818) → 2
count8(8818) → 4
```
Solutions:

```python
def count8(x: int) -> int:
    if x == 0:
        return 0
    if x % 100 == 88:
        return 2 + count8(x//10)
    return (x % 10 == 8) + count8(x//10)
```

### countAbc
Count recursively the total number of "abc" and "aba" substrings that appear in the given string.
```
countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
```
Solutions:
```python
def countAbc(str_: str) -> int:
    if len(str_) <= 2:
        return 0
    return (str_[:3] == "abc" or str_[:3] == "aba") + countAbc(str_[1:])
```

### countHi
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
```
countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
```
Solutions:
```python
def countHi(str_: str) -> int:
    if len(str_) == 0:
        return 0
    return (str_[:2] == "hi") + countHi(str_[1:])
```

### countHi2
Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.
```
countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
```
Solutions:
```python
def countHi2(str_: str) -> int:
    if len(str_) <= 1:
        return 0
    if str_[:3] == "xhi":
        return countHi2(str_[3:])
    return (str_[:2] == "hi") + countHi2(str_[1:])
```

### countPairs
We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.
```
countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
```
Solutions:

```python
def countPairs(str_: str) -> int:
    if len(str_) <= 2:
        return 0
    return (str_[0] in str_[2:]) + countPairs(str_[1:])
```
