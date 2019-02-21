# Exercises

## Modulus
Complete the following problems which make use of the modulus `%` operator.

1. In the shell, try to use integer division and modulus to convert minutes -> hours and minutes.
E.g., 63 minutes is 1 hour, 3 minutes.
    ```python
    >>> 63 // ?  # should give you hours
    >>> 63 % ?  # should give you minutes
    ```
2. Write a program that stores the number of minutes in a variable called `total_minutes`.
The program will calculate the number of whole hours in a variable called `hours` and leftover minutes
in a variable called `minutes`. Use the `print()` function to output the result. If this is
 too easy, try to output it in the format of `HH:MM` with leading zeros. 
 With [.format](http://lmgtfy.com/?q=python+.format+leading+zeros).
 or [f-strings](https://stackoverflow.com/a/42562236/9754461)
3. Lets say you have a game that keeps track of the number of frames in a variable called `frame_count`. 
Assume games run at 60 frames per second. If you want to have an enemy shoot a lazer every second, 
how many frames need to pass before the enemy shoots? List out three or four `frame_count`s that will allow
a lazer to be shot. What is the relationship with those numbers and division, remainder division, and the 
frames per second? Can you think of a way, mathematically, that will calculate when the enemy can fire?
4. Write a program to store the total number of cents. Call the variable `total_cents` and give it a value.
Compute from the total cents, the number of whole dollars and cents using integer division and modulus.
5. Play around in the shell and try to isolate the last 2 digits from a 3-digit number. The last one digit from any number. Now try to isolate a digit in the hundreds column. The tens column.
6. Modify the program above to tell the user how many pennies, nickles, dimes, quarters, loonies and toonies
that will be. The output should look something like:
    ```
    245 cents is:
    1 - toonie
    0 - loonie
    1 - quarter
    2 - dime
    0 - nickle
    0 - penny
    ```
7. There are `n` students in the class, and they are all given an id `0 to n-1`. Create a variable to 
store one student's id. E.g., `student_id = 35`. Assign them a group number
by using modulus. There will be 5 groups. The group numbers will be 0-4. The output should look like:
    **Example 1:**
    ```
    Student id: 9
    You are in group #4.
    ```
    **Example 2:**
    ```
    Student id: 6
    You are in group #1.
    ```
8. In the shell, experiment with any number, `n % 2`. What is the relationship between the result 
and whether the number is even or odd?
9. Having understood #7, how would you check if a number is a multiple of 3? 4? Test your hypotheses in 
the shell.

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

# Lists
## Lists 1
Create a program the will read in daily tempuratures for one week.
Create a list to store the names of the days of the week. Also create a list
to store the daily tempuratures for one week. Read this in from user input.

1. Create a test function that will test each of the following functions:
2. Create a function that will take a list of tempuratures and return the average.
3. Create a function that will take a list of tempuratures and return the highest temp.
4. Create a function that will take a list of tempuratures and return the lowest temp.
    - *Do not* use the `max` and `min` functions. You want to be able to code these yourself.
5. Create a main function that will read in the week's tempuratures and call each of the 
above functions with user-friendly prompts and messages.
6. Identify code that needs to be guarded with try-except.

Example output:
```
The greatest weekly-tempurature program, ever!

Please enter the tempuratures for the following days:
Sunday: h
Please enter a number.
Sunday: 1
Monday: 2
Tuesday: 3
Wednesday: 4
Thursday: 5
Friday: 6
Saturday: 7

The average for the week is 4.0 degrees.
The weelky high is 7.0 degrees.
The weekly low is 1.0 degrees.
```

# Error Handling
## Error Handling 1
From [Error Handling](https://colab.research.google.com/drive/1I9ss_cFN7tHDXkKWQgR6HI4FKGlqejz3#scrollTo=xvZPiVfPeef7&line=2&uniqifier=1) Colab.
1. Create a list of marks. Read in the list of marks (user input) with a while loop. The user should enter `-1` to stop asking for marks. Don't add this to the list.
2. Validate the input using `try-catch-else` to handle the possiblity of the user inputting an invalid integer.
3. Using a `for-loop`, add up all the marks. Print out the average mark. 
4. What happens when the first input from the user is `-1`? Fix this problem.
5. **ADVANCED**: 
    - Create a custom exception called `MarkRangeError`. If the mark is negative or beyond 100, `raise` this exception.
    - Catch this error differntly from the `ValueError` caused by the `int()` function when trying to convert invalid values to integers.

# Solutions
## Modulus Solutions
**1.**
```python
>>> 63 // 60
1
>>> 63 % 60   
3
```
 
**2.**

```python
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Hours: {hours}, Minutes: {minutes}")

# with formatting
print(f"{hours:02d}:{minutes:02d}")  
print("{:02d}:{:02d}".format(hours, minutes))
```
**3.**
The enemy should shoot if `frame_count` is `60, 120, 180, 240...`.
They are all multiples of `60`.
When you divide those numbers by `60` you should get a whole number. This means, there is no remainder.
When you use modulus on those numbers, the result is `0`. E.g., `120 % 60 == 0`. Any `frame_count` value 
that returns a result of `0` when you modulus 60, is a multiple of 60 and the game should therefore fire the lazer that frame.

```python
>>> 35 % 60 
35  # do NOT fire this frame
>>> 120 % 60
0  # FIRE!
>>> 121 % 60
1  # do NOT fire
>>> 3872220 % 60
0  # FIRE!
```

// TODO: finish answers for modulus
4. Write a program to store the total number of cents. Call the variable `total_cents` and give it a value.
Compute from the total cents, the number of whole dollars and cents using integer division and modulus.
5. Play around in the shell and try to isolate the last 2 digits from a 3-digit number. The last one digit from any number. Now try to isolate a digit in the hundreds column. The tens column.
6. Modify the program above to tell the user how many pennies, nickles, dimes, quarters, loonies and toonies
that will be. The output should look something like:
7. There are `n` students in the class, and they are all given an id `0 to n-1`. Create a variable to 
store one student's id. E.g., `student_id = 35`. Assign them a group number
by using modulus. There will be 5 groups. The group numbers will be 0-4. The output should look like:


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
def draw_sun(x, y):
    """Draws a sun (yellow ellipse) at a given x,y coordinate.
    
    Args:
        x (int): x co-ordinate
        y (int): y co-ordinate
    """
    noStroke()
    fill(YELLOW)
    ellipse(x, y, 100, 100)
```

## Lists 1 Solution
Check out a solution with [more exception handling](https://gist.github.com/MrGallo/4db54eda84eb05d8bfd1fe715bf12d5f).
```python
DAYS = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split()

def get_average(tempuratures):
    """Returns average tempurature from a list.
    Args: 
        tempuratures (:obj:`list` of :obj:`float`): List of tempuratures
    Returns:
        float: Average tempurature
    """
    if len(tempuratures) == 0:
        return None

    total = 0.0
    for temp in tempuratures:
        total += temp

    average = total / len(tempuratures)
    return average

def get_maximum(tempuratures):
    """Finds highest tempurature from a list.
    Args: 
        tempuratures (:obj:`list` of :obj:`float`): List of tempuratures
    Returns:
        float: Highest tempurature
    """
    if len(tempuratures) == 0:
        return None
    
    highest = tempuratures[0]
    for temp in tempuratures[1:]:
        if temp > highest:
            highest = temp
    
    return highest

def get_minimum(tempuratures):
    """Finds lowest tempurature from a list.
    Args: 
        tempuratures (:obj:`list` of :obj:`float`): List of tempuratures
    Returns:
        float: Lowest tempurature
    """
    if len(tempuratures) == 0:
        return None
    
    lowest = tempuratures[0]
    for temp in tempuratures:
        if temp < lowest:
            lowest = temp
    
    return lowest


def tests():
    # test average function
    assert get_average([]) == None, "Should return None from empty list."
    assert get_average([1, 2, 3]) == 2, "Should calc average."

    # test maximum function
    assert get_maximum([]) == None, "Should return None as max of empty list"
    assert get_maximum([5, 2, 7, 4]) == 7, "Should find max value from middle of list"
    assert get_maximum([1, 5, 3, 7]) == 7, "Should find max at end of list"

    # Test minimum function
    assert get_minimum([]) == None, "Should return None for empty list"
    assert get_minimum([5, 2, 7, -500]) == -500, "Should find min value from middle of list"
    assert get_minimum([4, 5, 3, 2]) == 2, "Should find min at end of list"

    print("Passed all tests!")


def main():
    print("The greatest weekly-tempurature program, ever!")
    print()
    print("Please enter the tempuratures for the following days:")

    weekly_tempuratures = []
    i = 0
    while i < len(DAYS):
        day = DAYS[i]
        try:
            temp = float(input(f"{day}: "))
        except:
            print("Please enter a number.")
        else:
            weekly_tempuratures.append(temp)
            i += 1
    
    print()

    average = get_average(weekly_tempuratures)
    print(f"The average for the week is {average} degrees.")

    highest = get_maximum(weekly_tempuratures)
    print(f"The weelky high is {highest} degrees.")

    lowest = get_minimum(weekly_tempuratures)
    print(f"The weekly low is {lowest} degrees.")


tests()
main()
```

## Error Handling 1 Solution
```python
marks = []
while True:
    try:
        mark = int(input("Enter a mark, -1 to stop: "))
    except:
        print("Invalid input")
    else:
        if mark == -1:
            break
        marks.append(mark)

total = 0
for mark in marks:
    total += mark
    
avg = total/len(marks)
print(f"The average is {avg}%")
```
