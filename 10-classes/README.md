# Classes Section Goals

- [Store data in an object](#store-data-in-an-object)
- [`__init__` method](#__init__-method)
- [Loop through a list of objects](#loop-through-a-list-of-objects)
- [Understand object pointers](#understand-object-pointers)
- [Know difference between a *class* and an *object*](#class-vs-object)
- [Instance method](#methods)
- [Encapsulation](#encapsulation)
- Aggregate class
- [Class field (variable)](#class-field)
- [Class method](#class-method)
- [Inheritance](#inheritance)
- Polymorphism
- Refactor multiple classes


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

## Methods
An example of methods. One without arguments, one with.
```python
class Person:
    def __init__(self, name, height, strength):
        self.name = name
    
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
       
    def compliment(self, person):
        print(f"{person.name}, I love your hair!")

# Usage
p1 = Person("Jeff")
p2 = Person("Sally")

p1.introduce()
p2.compliment(p1)

# output:
# "Hello, my name is Jeff."
# "Jeff, I love your hair!"
```

## Encapsulation
When writing a library or an API, your Classes attributes **must** be encapsulated. In short, provide *getters* and *setters* for each attribute. *Encapsulation* allows library authors to make fairly major changes to the inner-working of their classes without breaking the code of the programmers who use the labrary.

**NOT encapsulated**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Object attributes are accessed throught the *getter* methods and attributes are chaged throught the *setter* methods. This allows us to verify the data that gets passed to the attributes.


**Encapsulated**:
```python
class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, value: int):
        self._age = value
    
    def get_name(self):
        return self._name
    
    def set_name(self, value: str):
        self._name = value
```

## Class field
```python
from typing import List


class Pizza:
    num_pizzas = 0  # class field (variable)

    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings
        self.id = Pizza.num_pizzas
        Pizza.num_pizzas += 1  # update the class field
    
    def __str__(self) -> str:
        return f"{self.name}, toppings: {self.toppings}, id: {self.id}"
    

def main():
    pepperoni = Pizza.("Pepperoni", ["cheese", "pepperoni"])
    print(pepperoni)


if __name__ == "__main__":
    main()
```

## Class method
```python
from typing import List


class Pizza:
    num_pizzas = 0

    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings
        self.id = Pizza.num_pizzas
        Pizza.num_pizzas += 1
    
    def __str__(self) -> str:
        return f"{self.name}, toppings: {self.toppings}, id: {self.id}"
    
    @classmethod
    def pepperoni(cls):
        return cls("Pepperoni", ["cheese", "pepperoni"])
    
    @classmethod
    def cheese(cls):
        return cls("Cheese", ["cheese"])
    

def main():
    pepperoni = Pizza.pepperoni()
    print(pepperoni)

    cheese = Pizza.cheese()
    print(cheese)

    cheese_another = Pizza.cheese()
    print(cheese_another)

    print(Pizza.num_pizzas)


if __name__ == "__main__":
    main()
```

## Inheritance
```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def make_sound(self):
        print("<generic animal sound>")


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} the {self.breed}"
    
    def make_sound(self):
        print("Woof!")


class Squirrel(Animal):
    def make_sound(self):
        print("Squeek")


class Cat(Animal):
    pass


def main():
    d = Dog("Rover", "Dalmatian")
    s = Squirrel("Sammy")
    c = Cat("Bella")

    print(d)  # Rover the Dalmatian
    print(s)  # Sammy
    print(c)  # Bella

    d.make_sound()  # Woof!
    s.make_sound()  # Squeek
    c.make_sound()  # <generic animal sound>


if __name__ == "__main__":
    main()
```
