### 1
Create the class with the `__init__` method for the following.

```
Person
======
name: str
height: int
strength: int
health_points: int = 100
---------
__str__(self) -> str
introduce(self) -> void
punch(Person) -> void
```

```python
class Person:
    """
    Attrs:
        height (int): in cm
        name (str): First and last
        strength (int): How strong the person is 
        health_points (int): Out of 100 (everyone starts at 100)
    """
    def __init__(self, ...):
        pass
```

### 2
- Create two `Person` objects.

- Add a `__str__` (magic) method that displays the name and hp of the person.

- Print out each `Person` object.

### 3

- add an `introduce` method that will say "Hello, my name is {name}"

- Make both people objects introduce themselves.

### 4

- Add a `punch` method that will take another person as an argument, and subtract 10 from that person's hp.

- Make one `Person` object `punch` the other person object.

- Make one `Person` object punch themself.

### 5
- Add an `eat` method that, when used, will restor the health points back to 100.