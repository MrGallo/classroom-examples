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
6. Modify program #4 above to tell the user how many pennies, nickles, dimes, quarters, loonies and toonies
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

## Loops 1
1. Create a program that will ask the user for a word. The program will iterate through the string and print out each character except for the vowels.
2. Create a list of numbers. Create a program that will iterate through the list and print only the numbers greater than 10.
3. Create a list of numbers. Create a program that will iterate through the list and save the highest (maximum) value. Print out this value. Assume all numbers in the list are greater than 0.
4. Ask the user for their name. Create a program that will loop OVER A RANGE and print each character of their name on seperate lines. You will access each character by using the character's index value. E.g., char = name[0]

## Loops 2
1. Create a loop that will print "hello" 10 times.
2. Create a loop that will print out the multiples of 3 from 0 to 100.
   Hint: use Modulus
3. Create a loop that will add the numbers from 1-10. 1+2+3...+10

## Loops 3
Trace the following programs.
```python 
for num in range(5):
    double = num * 2
    print(double)
```
```python
for i in range(1, 6):
    a = i + 2
    print(i)

print(a)
```

## Loops - Convert for to while 1
```python

# 1
my_str = "hello"
for char in my_str:
    """For every character in the string my_str, print the character"""
    print(char)


# 2
numbers = [7, 7, 2, 7, 11]
for num in numbers:
    """For every number in the list of numbers, print the number."""
    print(num)

# 3
marks = [84, 89, 90, 45, 67]
for mark in marks:
    """For every mark in the list of marks, print the mark"""
    print(mark)

# 4
for i in range(10):
    """For every number in the range, print the number"""
    print(i)

# 5
for i in range(5, 100, 5):
    print(i)

# 6
for i in range(100, -1, -5):
    print(i)


```

## Loops - Graphics 1
1. Create a for loop that will draw five circles horizontally at the following x coordinates. 
   The y values, size and color of the circles could be anything. Use the `range()` function or a list.
   `[50, 100, 150, 200, 250]`.

## Loops - Graphics 2
The goal is to use a for loop to draw a row of pine trees on the window.

Follow the steps in order.

1. With arcade, draw one pine tree. A sketch might help cut down your guess-and-check time.
    Pine tree:
        - Brown triangle on the top
        - Dark green rectangle as the trunk

2. Factor out variables for the tree's x and y positions.
   When you change any of the x or y variable values, the WHOLE tree should move without distorting.
   
    **Example - Before:**
   
    ```python
    arcade.draw_circle_filled(50, 50, 25, arcade.color.BLUE)
    arcade.draw_circle_filled(70, 70, 25, arcade.color.BLUE)
    ```
        
    **Example - After:**
   
    ```python
    x = 50
    y = 50
    arcade.draw_circle_filled(x, y, 25, arcade.color.BLUE)
    arcade.draw_circle_filled(x+20, y+20, 25, arcade.color.BLUE)
    ```

3. Now determine roughly where on the screen you want to start your row of trees.
    - Write down the start coordinate (x and y).
    - Write down the end coordinate.
    - Write down how many pixels apart you want them.

4. Create a for loop that will iterate over a range() from your start point,
   to your end point, increasing by the amount of pixels they are apart.
   Place your tree code in the loop and use the loop variable as your tree's x location.

## Lists - Graphics (Under construction)
0. Create a for loop that will draw `10` vertical squares whose y-values are random and within the window. Look at [Python's `randrange()` or `randint()` functions](https://docs.python.org/3/library/random.html#random.randrange). You will notice an unexpected behaviour. The reason is the squares are being randomly assigned y-values *every* frame, which is 60 different y-values per second. We will deal with this in the next question. To keep the squares in the same position for each frame, you can only generate the random numbers once. Follow the steps to accomplish this:
    - The `setup()` function runs only once.
    - Create a **global** variable that holds an empty list. e.g., `y_values = []`.
    - In the `setup()` function use a loop to add 10 random values to the `y_values` list.
    - In the `draw()` function, use a loop to iterate through the `y_values` and draw the squares.
0. Create a program that will be the night sky. Black background and `100` stars. Randomly assign the star's x *and* y values. Be sure to create a global list like the question before.

## User Interface
0. Create a program that will store, in a two variables, the health points and maximum health points of an RPG character.
The program will draw a health bar. One rectangle

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

**4.**
```python
total_cents = int(input("Enter number of cents: "))

dollars = total_cents // 100
cents = total_cents % 100

print(f"{dollars} dollars and {cents} cents.")
```

**6.**
```python
cents = int(input("Enter the amount of cents: "))

toonies = cents // 200
cents = cents % 200  # calculate remaining cents after toonies

loonies = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickles = cents // 5
cents = cents % 5

pennies = cents

print(f"Toonies: {toonies}")
print(f"Loonies: {loonies}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickles: {nickles}")
print(f"Pennies: {pennies}")
```
// TODO: finish answers for modulus
7. There are `n` students in the class, and they are all given an id `0 to n-1`. Create a variable to 
store one student's id. E.g., `student_id = 35`. Assign them a group number
by using modulus. There will be 5 groups. The group numbers will be 0-4. The output should look like:

## Loops 1 Solutions

```python
# 1
word = "hello"
for char in word:
    if (char != "a" and char != "e" and char != "i" and
            char != "o" and char != "u"):
        print(char)

# 2
numbers = [5, 7, 2, 85, 1234, 32, 23]
for num in numbers:
    if num > 10:
        print(num)

# 3
numbers = [5, 7, 2, 85, 1234, 32, 23]
maximum = 0
# maximum = numbers[0]  # Better to get the first element of the list
for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)


# 4
name = "Frank"
for i in range(len(name)):
    print(f"index: {i}, char: {name[i]}")
```

## Loops 2 Solutions
```python
# 1
for i in range(10):
    print("hello")

# 2 a
for num in range(0, 101):
    if num % 3 == 0:
        print(num)

# 2 b
for num in range(3, 101, 3):
    print(num)

# 3
total = 0
for num in range(11):
    total += num
print(total)

```

## Loops - Convert for to while 1 Solution
```python
# 1
my_str = "hello"
i = 0  # counter variable
while i < len(my_str):
    char = my_str[i]  # access by index
    print(char)
    i += 1  # increase counter


# 2
numbers = [7, 7, 2, 7, 11]
i = 0
while i < len(numbers):
    num = numbers[i]
    print(num)
    i += 1

# 3
marks = [84, 89, 90, 45, 67]
i = 0
while i < len(marks):
    mark = marks[i] 
    print(mark)
    i += 1

# 4
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# 5
counter = 5
while counter < 100:
    print(counter)
    counter += 5

# 6
counter = 100
while counter >= 0:
    print(counter)
    counter -= 5


```


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
