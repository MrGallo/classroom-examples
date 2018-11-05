# Code Kata

## Variables and Printing
### 1.1
Create a program that acts as a calculator to help you do your math homework. Use an equation like: `y = ax**2 + bx + c` (Grade 12) or `y = mx + b` (Grade 10).
1. Hard code the whole print statement with literal numbers.
2. Factor out each variable, one at a time, running and testing along the way.
3. Once all variables have been factored out, you may add user input for the variables

## Loops
### 2.1
Create a program that will iterate (loop) over a string to find all occurances of the letter 'e'. When one is found, print "Found 'e' at index #". Start from the code below and convert to a for loop.
```python
my_string = "hello world"

if my_string[0] == 'e':
    print("Found e at 0")

if my_string[1] == 'e':
    print("Found e at 1")

if my_string[2] == 'e':
    print("Found e at 2")
```

### 2.2
Create a processing sketch that will draw multiple ellipses spread across the x axis. Start from the code below and convert to a for (or while) loop:
```python
size(640, 480)
background(255)

fill(0)
ellipse(50, height/2, 50, 50)
ellipse(200, height/2, 50, 50)
ellipse(350, height/2, 50, 50)
ellipse(500, height/2, 50, 50)
```

### 2.3 Add Evens
Create a program that will add only the even numbers from 10 to 10000.
Use a for loop and the range() function.

## Functions
### 3.1
1. Create a program that will take a name and and age.
2. Output a message in the format:
   "Hello, {name}, next year you will be {age} years old"
3. Convert to function. Call it "greet".
   - call the function below.
   - turn variables 'name' and 'age' into parameters.
   - instead of printing the result, return the result.

Start with:
```python
name = "Frank"
age = 13
message = f"Hello, {name}, next year you will be {age + 1} years old"
print(message)
```

# End results
End results are not the point of a code kata. It is the *process* you go through to arrive at the end that matters. Memorize that *process*, not the end result. 

### 1.1
#### Grade 10
```python
x = 4
m = 3
b = 5
y = m*x + b
print(y)
```
#### Grade 11
```python
x = 3
a = 5
b = 7
c = 9
y = a*x**2 + b*x + c
print(y)
```

### 2.1
```python
my_string = "hello world"

for index in range(len(my_string)):
    if my_string[index] == 'e':
        print("Found e at", index)
```

### 2.2
```python
size(640, 480)
background(255)

fill(0)

for x in range(50, 501, 150):
    ellipse(x, height/2, 50, 50)
```

### 2.3 Add Evens
```python
total = 0
for num in range(10, 10001, 2):
    total += num

print(total)
```

### 3.1
```python
def greet(name, age):
    message = "Hello, {}, next year you will be {} years old".format(name, age + 1)
    return message

greet_bob = greet("Bob", 15)
print(greet_bob)

print(greet("Frank", 33))
```
