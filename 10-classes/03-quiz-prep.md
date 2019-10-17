# Classes Quiz Prep

Topics:
- Annotate class and methods
- Docstrings for Class and methods
- Store data in an object
- `__init__` method
- Loop through a list of objects
- Understand object pointers
- Know difference between a class and an object
- Instance method

1. Create an `Item` class with the following details:
    ```
    Food
    ====
    name: str
    cost: int
    nutrition: int
    ```

2. Create a `Dog` class with the following details:
    ```
    Dog
    ====
    breed: str
    name: str
    happiness: int
    -----
    __str__() -> str
    eat(Food) -> void
    bark() -> void
    ```
    - The `eat` method will increase a Dog's happiness by `10%` of the food's nutrition.
    - The `bark` method will simply print "bark".
    - The `__str__` method will print out the dog's namd and happiness, formatted nicely.

3. Create a `main()` function to use and test out the two classes, be sure to showcase all the functionality.
4. Be sure to make a docstring for the class and annotate/docstring any methods in the class.
