# If Statements Section Goals

- [Know all comparison operators](#comparison-operators)
- Compare the value of an integer variable
- Compare the value of a string variable
- Compare the value of a boolean variable
- [Use `if/else`](#ifelse)
- [Use `if/elif/else`](#ifelifelse)
- [Use multiple `elif`](#multiple-elif)
- Store the result of a Boolean expression in a variable
- [Know Boolean operators and their truth tables](#boolean-operators)
- [Use Boolean operators in if statements](#boolean-operators-in-if-statements)
- Refactor `if` structures

## Comparison operators
```python
>   # greater than
<   # less than
>=  # greater than or equal to
<=  # less than or equal to
==  # equal to
!=  # not equal to
is
in
```

## `if/else`
```python
age = int(input("Please enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You can not vote.")
```

## `if/elif/else`
```python
mark = int(input("Please enter your mark: "))

if mark >= 80:
    print("You have an A")
elif mark >= 70:
    print("You have a B")
else:
    print("You have a C or lower.")
```

## Multiple `elif`
```python
mark = int(input("Please enter your mark: "))

if mark >= 80:
    print("You have an A")
elif mark >= 70:
    print("You have a B")
elif mark >= 60:
    print("You have a C")
elif mark >= 50:
    print("You have a D")
else:
    print("You FAIL!!!!")
```

## Boolean values in variables
[Video](https://youtu.be/mb-BSeRHQZw)
```python
a = 5

is_sunny = a > 5

if is_sunny is False:
    print("Grab your umbrella")
```

## Boolean operators
[Video](https://youtu.be/inxWNWy1nMA)

We need to be able to reproduce these truth tables.

### AND
For `and`, both conitions need to evaluate to `True`.

| A | B | A and B |
|:-:|:-:|:-------:|
| T | T | T       |
| T | F | F       |
| F | T | F       |
| F | F | F       |

### OR
For `or`, only one condition needs to evaluate to `True`.

| A | B | A or B |
|:-:|:-:|:------:|
| T | T | T      |
| T | F | T      |
| F | T | T      |
| F | F | F      |

### NOT
`Not` will invert the Boolean value.

| A | not A |
|:-:|:-----:|
| T | F     |
| F | T     |

## Boolean operators in if statements
```python
a = 5
b = 7

if a >= 5 and b > 10:  # False
    print("hello")

if a == 5 or b > 100:  # True
    print("goodbye")

if not (a >= 5 and b > 10):  # True
    print("hello")
```

