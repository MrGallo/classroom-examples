# Exercises
## Functions 1

Create a function:
1. called `say_hello` that takes no arguments,
   prints `hello`, and returns nothing.
2. called `say_hello_to` that takes a name, 
   prints `Hello {name}`, and returns nothing.
3. called `double` that takes an integer as an argument,
   and returns double its value.
4. called `last_first` that takes a first name and
   a last name. It will return the name in the format
   `{last_name}, {first_name}`.
5. called `is_dead`, that takes the number of incorrect
   guesses as an argument. Return true if incorrect guesses
   is greater than or equal to 6. False otherwise.

Your code should pass the following assertions:
```python
# 1
print("Should print 'hello'")
say_hello()

# 2
print("Should say 'Hello David'")
say_hello_to("David")

# 3
assert double(4) == 8, "Should return 8"
assert double(2) == 4, "Should return 4"

# 4
assert last_first("John", "Smith") == "Smith, John"
assert last_first("a", "b") == "b, a"

# 5
assert is_dead(5) == False, "Should not be dead"
assert is_dead(6) == True, "Should be dead"
assert is_dead(1001) == True, "Should be very dead"
```
## Functions 2
1. Define a function called draw_player that simply prints the statement "Drawing player...". Call the function (so it would execute).
2. Define a function called draw_sun. It will take an x and y location. It will print a message "Drawing sun at ({x}, {y}).". (Insert the argument values into the string). Call this function too.

## Functions 3
Complete the `draw_sun` function according to the PyDoc.
```python
SKY_BLUE = color(0, 191, 255)
YELLOW = color(255, 255, 0)

def setup():
    size(640, 480)


def draw():
    background(SKY_BLUE)
    draw_sun(50, 100)


def draw_sun():
    """Draws a sun (yellow ellipse) at a given x,y coordinate.
    
    Args:
        x (int): x co-ordinate
        y (int): y co-ordinate
    """
    pass
```

# Solutions
## Functions 1 Solution
```python
def say_hello():
    """1. called 'say_hello' that takes no arguments,
    prints 'hello', and returns nothing.
    """
    print("hello")


def say_hello_to(name):
    """2. called 'say_hello_to' that takes a name, 
    prints 'Hello {name}', and returns nothing.
    """
    print("Hello " + name)


def double(n):
    """3. called 'double' that takes an integer as an argument,
    and returns double its value.
    """
    return n * 2


def last_first(first, last):
    """4. called 'last_first' that takes a first name and
    a last name. It will return the name in the format
    '{last_name}, {first_name}'.
    """
    return "{}, {}".format(last, first)


def is_dead(incorrect_guesses):
    """5. called 'is_dead', that takes the number of incorrect
    guesses as an argument. Return true if incorrect guesses
    is greater than or equal to 6. False otherwise.
    """
    return incorrect_guesses >= 6
```
## Functions 2 Solution
```python
def draw_player():
    """Define a function called draw_player that simply 
    prints the statement "Drawing player...". 
    Call the function (so it would execute).
    """
    print("Drawing player...")


def draw_sun(x, y):
    """Define a function called draw_sun. It will take an x and y location. 
    It will print a message "Drawing sun at ({x}, {y}).". 
    (Insert the argument values into the string). 
    Call this function too.
    """
    print(f"Drawing sun at ({x}, {y}).")


draw_player()
draw_sun(50, 150)
```

## Functions 3 Solution
```python

```
