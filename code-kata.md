# Code Kata

## Variables and Printing
### 1.1
Create a program that acts as a calculator to help you do your math homework. Use an equation like: `y = ax**2 + bx + c` (Grade 12) or `y = mx + b` (Grade 10).
1. Hard code the whole print statement with literal numbers.
2. Factor out each variable, one at a time, running and testing along the way.
3. Once all variables have been factored out, you may add user input for the variables

## Functions
### 3.1
1. Create a program that will take a name and and age.
2. Output a message in the format:
   "Hello, {name}, next year you will be {age} years old"
3. Convert to function. Call it "greet".
   - turn variables 'name' and 'age' into parameters.
   - instead of printing the result, return the result.
   - call the function below.

## End results
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

### 3.1
```python
def greet(name, age):
    message = "Hello, {}, next year you will be {} years old".format(name, age + 1)
    return message

greet_bob = greet("Bob", 15)
print(greet_bob)

print(greet("Frank", 33))
```
