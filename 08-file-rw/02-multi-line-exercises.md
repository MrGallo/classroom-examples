# Multi-line exercises

Create a multi-line text file with one word on each line

## Exercises
1. Open the text file and print out `f.read()`. What does it look like?
2. Use a for loop to print out each line individually. `for line in f:`
3. Print out only the words that start with "m", or some other specific letter.

## Solutions
### 1
```python
with open("some_file.txt", "r") as f:
    print(f.read())
```
### 2
```python
with open("some_file.txt", "r") as f:
    for line in f:
        print(line.strip())
```
### 3
```python
with open("some_file.txt", "r") as f:
    for line in f:
        if line.lower().startswith("m"):
            print(line.strip())
```
