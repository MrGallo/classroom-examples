# Classes Section Goals

- [Store data in an object](#store-data-in-an-object)
- [Know difference between a *class* and an *object*](#class-vs-object)
- Access instance variables
- `__init__` method
- Instance method
- Class method
- Inheritance
- Refactor multiple classes
- Aggregate class
- Class variable


## Store data in an object
```python
class Person:
    pass


p = Person()
p.name = "Jeff"
p.age = 45

print(f"Hello {p.name}, you are {p.age} years old!")
```

## Class vs Object
- *Object*: A specific instance of a thing. e.g., "Jeff"
- *Class*: the general thing. e.g., "a person"
```python
class Person:
    def __init__():
        self.name = None
        self.age = None


jeff = Person()     # Jeff is a person
jeff.name = "Jeff"  # All persons have a name
jeff.age = 35       # All persons have and age
```
