# Classes Section Goals

- [Store data in an object](#store-data-in-an-object)
- [`__init__` method](#__init__-method)
- [Loop through a list of objects](#loop-through-a-list-of-objects)
- [Understand object pointers](#understand-object-pointers)
- [Know difference between a *class* and an *object*](#class-vs-object)
- Access instance variables
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

print(f"This is {p.name}, they are {p.age} years old!")
```

## `__init__` method
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


jeff = Person("Jeff", 35)
print(f"This is {jeff.name}, they are {jeff.age} years old!")
```

## Loop through a list of objects
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# --- OK ---
# Store each person object in a vriable, then add them to a list.
# This has its limitations.
jeff = Person("Jeff", 35)
sally = Person("Sally", 30)
ben = Person("Ben", 22)

people = [jeff, sally, ben]

# --- BETTER ---
# Create the person objects directly in a list
people = [Person("Jeff", 35), Person("Sally", 30), Person("Ben", 22)]

for p in people:
    print(f"This is {p.name}, they are {p.age} years old!")
```

## Understand object pointers
For **primitive datatypes**, literal values are stored in variables.
```python
a = 5
b = a  # COPY the VALUE of `a` and store it in `b`

print(a)  # 5
print(b)  # 5

a += 3

print(a)  # 8
print(b)  # 5
```

For, **objects** the memory location (pointer) is stored in variables.
```python
class Person:
    pass

a = Person()  # create a person object, store the pointer in variable `a`
a.name = "Frank"

print(a.name)  # "Frank"

b = a          # Copies the POINTER, not the data
print(b.name)  # "Frank"

print(a)  # <__main__.Person object at 0x0000016E2BE44550>
print(b)  # <__main__.Person object at 0x0000016E2BE44550> (same memory location)

a.name = "Sally"
print(a.name)  # "Sally"
print(b.name)  # "Sally"
```
Both variables `a` and `b` **point** to the same object.

## Class vs Object
- *Object*: A specific instance of a thing. e.g., "Jeff"
- *Class*: the general thing. e.g., "a person"

