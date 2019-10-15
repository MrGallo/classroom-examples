class Person:
    """
    Attrs:
        height (int): in cm
        name (str): First and last
        strength (int): How strong the person is 
        health_points (int): Out of 100 (everyone starts at 100)
    """
    def __init__(self, name, height, strength):
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = 100
    
    def __str__(self):
        return f"{self.name}, hp: {self.health_points}"


jeff = Person("Jeff Blah", 170, 1)
david = Person("David Greenchair", 200, 1)

print(jeff)
print(david)
