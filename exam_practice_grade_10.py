"""
1. Using a variable for length and a variable for width,
create a program that will calculate the area of a rectangle,
storing it in a variable and outputting the result (without units).
"""
length = 5
width = 2
area = length * width
print(area)


"""
2. Ask the user to input a number from 1-5 rating a restaurant's service.
Depending on what they rate the restaurant, the program will output an
appropriate message from:
1 -> "We are very sorry" to
5 -> "Great! We are glad you enjoyed yourself!".
"""
rating = int(input("Please enter a rating (1-5) for the restaurant: "))
if rating == 5:
    print("Great! We are glad you enjoyed yourself!")
elif rating == 4:
    print("Thank you, see you next time!")
elif rating == 3:
    print("We hope to exceed your expectations next time.")
elif rating == 2:
    print("Please let us know what we could do better.")
elif rating == 1:
    print("We are very sorry.")


"""
Create a program that will give the user the option to choose from a
small(8.99), medium(10.99) and large(12.99) pizza as well as the quantity.
Calculate and display the subtotal, the tax and the grand total.
"""
size = input("What type of pizza? (small, medium, large): ")
quantity = int(input("How many do you want? "))

if size == "small":
    price = 8.99
elif size == "medium":
    price = 10.99
elif size == "large":
    price = 12.99

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax
print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {total}")


"""
Create a loop to add the numbers from variable a to variable b.
You can fill in their literal values.
"""
a = 5
b = 11
total = 0
for n in range(a, b+1):
    total += n

print(total)

# while loop
i = a
while i < b+1:
    total += n
    i += 1


"""
Given some string variable, create a new string that is made up of
every other character in the original string. Use a loop to do this.
"""
some_string = "Hello, World!"
new_string = ""
for i in range(0, len(some_string), 2):
    new_string += some_string[i]

print(new_string)

# while loop
i = 0
while i < len(some_string):
    new_string += some_string[i]
    i += 2


"""
Given some string, create a new string that is a copy of the
original string but without vowels. Use a loop to do this.
"""
some_string = "Hello, World!"
new_string = ""

for char in some_string:
    if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
        new_string += char

# simpler
for char in some_string:
    if char not in "aeiou":
        new_string += char
