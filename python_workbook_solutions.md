# The Python Workbook
Missing solutions and Mr. Gallo solutions

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


def test_hypotenuse():
    assert hypotenuse(3, 4) == 5
    assert hypotenuse(6, 8) == 10
    print("Passed all tests", end="\n\n")


def main():
    print("Welcome to the Hypotenuse calculator")
    a = float(input("Enter side A:"))
    b = float(input("Enter side B:"))
    hypot = hypotenuse(a, b)
    print("The hypotenuse is: {}".format(hypot))


# test_hypotenuse()
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
