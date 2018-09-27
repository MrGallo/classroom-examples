# Test Solutions

## Chapter 3 Quiz (Makeup)
**#5.** Write a program that takes user input asking the user for their name and age. 
The program will output a message exactly in the format: `"Hello, {name}, next year you will be {age} years old!"`
```python
name = input("Please enter yor name:")
age = int(input("Please enter your age:"))
message = "Hello, {}, next year you will be {} years old!".format(name, age+1)
print(message)
```

**#6.** Write a program that will take the length and width of a 
rectangle as user input and output it's area. 
```python
length = float(input("length:"))
width = float(input("width:"))
area = length * width
print(f"The area is {area} units squared.")
```
