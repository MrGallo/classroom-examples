# The Python Workbook
The Missing Solutions

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

def calc_fare(distance):  # add distance parameter
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
    fare = calc_fare(distance_in_km)  # pass the distance to the function
    print("The total fare is ${}.".format(fare))

# tests()
main()
```
