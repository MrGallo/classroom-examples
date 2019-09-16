# Introduction Section Goals
Every program will involve some *input, processing, and output*.
- [Create a python file and output a message](#create-and-run-a-python-file)
- [Storing data in variables](#storing-data-in-variables)
- [Get input from user](#get-input-from-user)
- [Convert input to number](#convert-input-to-number)
- [Format output text](#format-output-text)
- [Create a main function and output a message](#create-a-main-function)
- [Calling Functions Within Functions](#calling-functions-within-functions)

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

```

## Format output text
```python

```

## Create a `main` function
[Video](https://youtu.be/mEL944nYaEQ)

```python
def main():
    print("Hello!")
    print("Blah")
    print(5 + 6)
    print(400 / 6 * 2)
    print(5 + 7 * 8)


if __name__ == "__main__":
    main()
```

## Calling Functions Within Functions 
[Video](https://youtu.be/vGnLqC-9YBY)
Create a `main` function. Create two other functions that output different 
messages and call them from within the `main` function.
```python
def main():
    say_hello()
    say_goodbye()

    say_hello()
    say_goodbye()


def say_hello():
    print("Hello")


def say_goodbye():
    print("Goodbye.")


if __name__ == "__main__":
    main()
```

*Output:*
```
Hello
Goodbye.
Hello
Goodbye.
```
