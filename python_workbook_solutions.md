# The Python Workbook
Missing solutions and Mr. Gallo solutions

- [Introduction to Programming](#introduction-to-programming)
  * [Exercise 1: Mailing Address](#exercise-1--mailing-address)
  * [Exercise 2: Hello](#exercise-2--hello)
  * [Exercise 4: Area of a Field](#exercise-4--area-of-a-field)
  * [Exercise 5: Bottle Deposits](#exercise-5--bottle-deposits)
- [If Statements](#if-statements)
  * [Exercise 34: Even or odd?](#exercise-34--even-or-odd-)
  * [Exercise 35: Dog Years](#exercise-35--dog-years)
  * [Exercise 36: Vowel or Consonant](#exercise-36--vowel-or-consonant)
- [Functions](#functions)
  * [Exercise 81: Compute the Hypotenuse](#exercise-81--compute-the-hypotenuse)
  * [Exercise 82: Taxi Fare](#exercise-82--taxi-fare)
- [Lists](#lists)
  * [Exercise 105: Reverse Order](#exercise-105--reverse-order)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Introduction to Programming
### Exercise 1: Mailing Address
I suggest first printing the information of the school (not your personal information). Then, refactoring those strings into variables. Do not store formatting characters (spaces and commas) in your variables!

**Part 1 Solution:**
```python
print("St. Robert Catholic High School")
print("8101 Leslie St.")
print("Thornhill, ON")
print("L3T 7P4")
print("905-889-4982")
```
**Part 2 Solution:**
```python
name = "St. Robert Catholic High School"
address = "8101 Leslie St."
city = "Thornhill"
province = "ON"
postal_code = "L3T 7P4"
telephone = "905-889-4982"

print(name)
print(address)

print(f"{city}, {province}")
print("{}, {}".format(city, province))
# which formatting method do you prefer?

print(postal_code)
print(telephone)

```
### Exercise 2: Hello
```python
name = input("Please enter your name: ")
print(f"Hello, {name}. Nice to meet you!")

# ---- Extra ----
mood = input("How are you feeling? ")

# ----- ADVANCED----
if mood == "good":
    print("Blessed.")
elif mood == "bad":
    print("Aww. It will get better!")
elif mood == "criminal":
    print("Calling police...")
else:
    print("Ok. Bye.")

```

### Exercise 4: Area of a Field
```python
print("Calculate the acreage of a field.")
print("Enter dimensions in feet.")

length = int(input("Length: "))
width = int(input("Width: "))

sq_feet = length * width
acres = sq_feet / 43560

print(f"The field is {acres} acres.")
```

### Exercise 5: Bottle Deposits
```python
print("Bottle Refund Calculator")
print("=" * 24)
print()

num_small = int(input("Enter number of small bottles: "))
num_large = int(input("Enter number of large bottles: "))

refund_small = num_small * 0.10
refund_large = num_large * 0.25
refund_total = refund_small + refund_large

print()
print("Refund: ${}".format(refund_total))
```

## If Statements
### Exercise 34: Even or odd?
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Exercise 35: Dog Years
```python
# get age of dog (in years)
age = float(input("How old is your dog? "))

# if the age is negative, display an error message
if age < 0:
    print("Invalid number!")
else:
    if age <= 2:
        dog_years = age * 10.5
    else:
        first_two = 2 * 10.5
        remaining_years = age - 2

        dog_years = first_two + remaining_years * 4
    
    print(f"Your dog is {dog_years} years old in dog-years.")
```

### Exercise 36: Vowel or Consonant
```python
letter = input("Enter a letter: ")

if letter == "a":
    print("Vowel")
elif letter == "e":
    print("Vowel")
elif letter == "i":
    print("Vowel")
elif letter == "o":
    print("Vowel")
elif letter == "u":
    print("Vowel")
elif letter == "y":
    print("Y is sometimes a vowel")
else:
    print("Consonant")
```

## Functions
### Exercise 81: Compute the Hypotenuse
```python
from math import sqrt


def hypotenuse(a, b):
    """Returns the length of the hypotenuse of a right-angle triangle.

    Args:
        a (float): Length of side A
        b (float): Length of side B

    Return:
        float: length of Hypotenuse
    """
    return sqrt(a*a + b*b)


def main():
    print("Welcome to the Hypotenuse calculator")
    a = float(input("Enter side A:"))
    b = float(input("Enter side B:"))
    hypot = hypotenuse(a, b)
    print("The hypotenuse is: {}".format(hypot))


if __name__ == "__main__":
    main()
```

### Exercise 82: Taxi Fare
```python
BASE_FARE = 4.00
RATE_PER_140_METERS = 0.25


def calc_fare(distance):
    """Calculates taxi fare based on distance traveled (km)
    Args:
        distance (float): Distance traveled in Kilometers.
    Return:
        float: The fare for the taxi ride.
    """
    return BASE_FARE + RATE_PER_140_METERS * (distance // 0.140)


def tests():
    assert calc_fare(0) == BASE_FARE, "Should charge base-fare."
    assert calc_fare(0.05) == BASE_FARE, "Should not round up until you reach 140 meters."
    assert calc_fare(0.14) == BASE_FARE + RATE_PER_140_METERS, "Should add the first 25 cents."
    assert calc_fare(0.28) == BASE_FARE + 2*RATE_PER_140_METERS, "Should add the second 25 cents."
    print("Passed all tests!")


def main():
    print("Welcome to the fare calculator.")
    distance = float(input("Enter the number of meteres traveled:"))
    distance_in_km = distance / 1000
    fare = calc_fare(distance_in_km)
    print("The total fare is ${}.".format(fare))

tests()
main()
```
## Lists
### Exercise 105: Reverse Order
```python 
numbers = []

while True:
    num = int(input("Enter a number, 0 to stop: "))
    if num == 0:
        break
    numbers.append(num)

# loop over reversed list
for number in reversed(numbers):
    print(number)

# for loop over the range from len-1 to 0
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])

# while loop
i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1

# for loop over slice
for number in numbers[::-1]:
    print(number)
```
