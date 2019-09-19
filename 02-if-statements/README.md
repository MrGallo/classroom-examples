# If Statements Section Goals

- [Know all comparison operators](#comparison-operators)
- Compare the value of an integer variable
- Compare the value of a string variable
- Compare the value of a boolean variable
- [Use `if/else`](#ifelse)
- [Use `if/elif/else`](#ifelifelse)
- [Use multiple `elif`](#multiple-elif)
- Store the result of a Boolean expression in a variable
- Know Boolean operators and their truth tables
- Use Boolean operators in if statements
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