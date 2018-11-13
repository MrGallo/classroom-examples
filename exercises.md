# Exercises
## Functions
### 1

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

# Solutions
## Functions
### 1
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
