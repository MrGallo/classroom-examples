
# ----- 1 -------
name = "Dave"

print(f"Hello, {name}!")
print("Hello, {}!".format(name))
print("Hello", name, "!")
print("Hello " + name + "!")

# ---- 2 -----
m = 10
x = 5
b = 1
y = m * x + b
print(f"When x is {x}, y is {y}.")

# ----- 3 -------
length = 5
width = 10
area = length * width
perimeter = (length + width) * 2

print("Area: {}, Perimeter: {}".format(area, perimeter))

# -------- 4 -------
people = 2
avg_slices = 3
slices_per_pizza = 8
slices_needed = people * avg_slices
pizzas = slices_needed / slices_per_pizza

print(f"You need {pizzas} pizzas")


