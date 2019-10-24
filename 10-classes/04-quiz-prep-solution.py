class Food:
    """Food class

    Attributes:
        name (str): the name of the food
        cost (int): how much the food costs
        nutrition (int): how nutritious the food is
    
    """
    def __init__(self, name: str, cost: int, nutrition: int):
        """Create a Food object.

        Args:
            name: the name of the food
            cost: how much the food costs
            nutrition: how nutritious the food is
        """
        self.name = name
        self.cost = cost
        self.nutrition = nutrition


class Dog:
    """Thing that goes "roof"
    
    Attributes:
        breed (str): The dog's breed.
        name (str): The dog's name.
        happiness (int): Happiness value of the dog. Defaults to 100.
    """
    def __init__(self, breed: str, name: str):
        """Create a Dog object.

        Args:
            breed: The breed of the dog.
            name: The dog's name.
        """
        self.breed = breed
        self.name = name
        self.happiness = 100

    def __str__(self) -> str:
        return f"{self.name}, happiness: {self.happiness}"
    
    def eat(self, food: Food):
        """Get the dog to eat some food.
        
        Increasing the dog's happiness by 10% of the food eaten.

        Args:
            food: The food for the dog to eat.
        """
        happiness_increase = food.nutrition * 0.1
        self.happiness += happiness_increase
    
    def bark(self):
        """Make the dog bark."""
        print("RUFF RUFF!")

def main():
    sausage = Food("Polish Sausage", 10, 100)
    fido = Dog("Husky", "Fido")

    print(fido.happiness)

    fido.eat(sausage)

    print(fido.happiness)

    fido.bark()

    print(fido)


if __name__ == "__main__":
    main()
