# Functions Practice
Create complete the following functions as described in the Doc Strings. Annotate the function's parameters and return type. For example:
```python
def some_function(n: int, string: str) -> str:
    """Does something.
    
    Args:
        n (int): Some number.
        string (str): Some string
       
    Returns:
        str: A vague string.
    """
```

**Also**, for each function. Think of three test cases. For now, just call the function and expect a result, like we see in codingbat. 
For example if your function is called add and it adds three numbers the tests would look like:
```
add(5, 6, 7) -> 18
add(0, 0, 0) -> 0
add(1, 2, 3) -> 5
```

## The Functions
```python
from typing import List


from typing import List


def add(a: float, b: float) -> float:
    """Adds two numbers.
    
    Args:
        a (float): A number.
        b (float): Another number.
    
    Returns:
        float: The sum of the two numbers.
    """
    return a + b


assert add(1, 1) == 2
assert add(1, 2) == 3
assert add(5, 4) == 9


def format_name(first: str, last: str) -> str:
    """Formats a name in 'Last, First' format.

    For example: "Smith, John"

    Args:
        first (str): The first name.
        last (str): The last name.
    
    Returns:
        str: The formatted name.
    """
    return f"{last}, {first}"


assert format_name("John", "Smith") == "Smith, John"
assert format_name("a", "b") == "b, a"
assert format_name("123", "456") == "456, 123"


def strip_phone_number(phone_number: str) -> str:
    """Remove all characters but integers from a phone number.

    Numbers entered by users can be given in a variety of formats.
    For example a user may enter their number as 901234567, or 905.123.4567 or
    (905)123-4567 or 905 123 4567. A database system should store numbers in a
    consistent format.

    The format we are looking for is just digits. E.g., 9051234567.

    Args:
        phone_number (str): A user-entered phone number in need of re-formatting.
    
    Returns:
        str: The phone number stripped to just it's digits.
    """
    new_str = ""
    for c in phone_number:
        if c in "0123456789":
            new_str += c
        
    return new_str


assert strip_phone_number("(905)123-4567") == "9051234567"
assert strip_phone_number("(905)))1..,/.,$%^&*23-----4567") == "9051234567"


def format_phone_number(phone_number: str) -> str:
    """Formats a phone number to (000)000-0000.

    Args:
        phone_number (str): A 10 digit phone number as a string.
            For example: "9051234567"
    
    Returns:
        str: The formatted phone number.
    """
    first = phone_number[:3]
    middle = phone_number[3:6]
    last = phone_number[-4:]
    return "({}){}-{}".format(first, middle, last)

assert format_phone_number("9053337676") == "(905)333-7676"


def add_from_list(numbers: List[int], a: int, b: int) -> int:
    """Adds two values from a list at index a and b.
    
    Args:
        numbers (List[int]): a list of numbers.
        a (int): the first index location.
        b (int): the second index location.

    Returns:
        int: The two values at index a and b added together.
    """
    return numbers[a] + numbers[b]


assert add_from_list([1, 2, 3], 0, 2) == 4
assert add_from_list([5, 3, 1], 2, 2) == 2
assert add_from_list([6, 2, 76, 3, 2, 5, 2, 6, 3, 3, 2, 4, 6, 7, 543, 6, 8, 4, 3, 7, 65, 4], -1, 0) == 10
```
