# Quiz 1 Solutions

1. Write a program that will prompt the user for their name.
The program will simply output their name back to them.

    ```python
    name = input("Please enter your name: ")
    print(name)
    ```


2. Write a program that will ask the user for a length and a width of a rectangle.
The program will prompt the user for the input, 
it will make the calculation for area (store that into a variable),
and then output a message to the user revealing to them the area.

    ```python
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))

    area = length * width

    print(f"The area is {area} units squared.")
    ```

3. Write a program that will ask the user for how many people will be at a party.
It will also ask, on average, how many slices each person might eat.
The program will output the number of pizzas to order.
Round the number using the round() function.
There are 8 slices in a pizza.

    ```python
    SLICES_PER_PIZZA = 8

    people = int(input("How many people? "))
    slices_per_person = int(input("How many slices per person? "))
    total_slices = people * slices_per_person
    total_pizzas = round(total_slices / SLICES_PER_PIZZA)  # use math.ceil for better results

    print(f"You will need {total_pizzas} pizzas.")
    ```
