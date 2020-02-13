Create a mailing label and extract all the data that could vary.
```python
name = "Mr. Gallo"
number = 999
street = "Blah Road"
city = "Concord"
province = "ON"
postal_code = "L3T 7P4"

print(name)
print(f"{number} {street},")
print(f"{city}, {province}")
print(postal_code)
```

Ask the user for their name and place it in a message.
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```
