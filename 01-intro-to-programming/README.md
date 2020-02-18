# Introduction Section Goals
Every program will involve some *input, processing, and output*.
- [Create a python file and output a message](#create-and-run-a-python-file)
- [Storing data in variables](#storing-data-in-variables)
- [Get input from user](#get-input-from-user)
- [Convert input to number](#convert-input-to-number)
- [Format output text](#format-output-text)

## Topics
- Variables
    - Assignment operator
    - Variables as containers
- Datatypes
    - Integer
    - Float
    - String
    - Boolean
- Output
    - f-strings
    - `.format()`
- Input
    - Prompting
    - Type conversion
    
## Projects
- Math formula calculator
- Madlibs
- Point of Sale (quantity and total + make change)
- Arcade
    - artwork with variables
    - simple animation
    
## Create and Run a Python File
[video](https://youtu.be/9TnvlIEgGVI)

## Storing Data in Variables
[Video](https://youtu.be/WUH_Yyr1YV8)
```python
length = 5
width = 10

area = length * width

print(area)  # 50
```

## Get input from user
[Video](https://youtu.be/zWbOxihFwJs)
```python
name = input("Please enter a name: ")

print("Hello", name)
```

## Convert input to number
```python
my_str = "hello"  # obviously a string
another_str = "500"  # not-so-obviously a string.
print(another_str + 2)  # will NOT work. Cannot do math on a string.

# we can convert strings that contain numbers into integers
print(int(another_str) + 2)

# we can also convert into float (decimal)
print(float(another_str) + 2)

# if receiving a number from user, convert it before storing it in a variable
some_number = int(input("Please enter a number: ))
```

## Format output text
There are a number of ways to format text by placing variable values into strings. All have their advantages and disadvantages.
```python
name = "John"
age = 37

# f-strings. Python 3.6+
message_fstring = f"Hello, {name}. You are {age} years old."

# .format()
message_dot_format = "Hello, {}. You are {} years old.".format(name, age)

# concatenation
message_concat = "Hello, " + name + ". You are " + str(age) + " years old."

# All output the exact same thing
# Hello, John. You are 37 years old.
print(message_fstring)
print(message_dot_format)
print(message_concat)
```
