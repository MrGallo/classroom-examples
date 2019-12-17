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


def add():
    """Adds two numbers.
    
    Args:
        a (float): A number.
        b (float): Another number.
    
    Returns:
        float: The sum of the two numbers.
    """
    pass  # pass is a place holder. remove this.


def format_name():
    """Formats a name in 'Last, First' format.

    For example: "Smith, John"

    Args:
        first (str): The first name.
        last (str): The last name.
    
    Returns:
        str: The formatted name.
    """
    pass


def strip_phone_number():
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
    pass


def format_phone_number():
    """Formats a phone number to (000)000-0000.

    Args:
        phone_number (str): A 10 digit phone number as a string.
            For example: "9051234567"
    
    Returns:
        str: The formatted phone number.
    """
    pass


def add_from_list():
    """Adds two values from a list at index a and b.
    
    Args:
        numbers (List[int]): a list of numbers.
        a (int): the first index location.
        b (int): the second index location.

    Returns:
        int: The two values at index a and b added together.
    """
    pass  

```
