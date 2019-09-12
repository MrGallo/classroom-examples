# Dictionaries Section Goals

- Create a dictionary
- Access dictionary values
- Insert into dictionary
- Modify dictionary values
- Remove dictionary values
- Loop over dictionary keys
- Loop over dictionary values
- Loop over dictionary values and keys

# Create, access, modify, insert, remove
```
>>> d = {}
>>> d
{}
>>> type(d)
<class 'dict'>
>>> d = {"first_name": "John"}
>>> d
{'first_name': 'John'}
>>> d["first_name"]
'John'
>>> d["last_name"] = "Smith"
>>> d
{'first_name': 'John', 'last_name': 'Smith'}
>>> d["first_name"]
'John'
>>> d["last_name"]
'Smith'
>>> d["grade"] = 12
>>> d
{'first_name': 'John', 'last_name': 'Smith', 'grade': 12}
>>> d["fav_food"] = "Pizza"
>>> d
{'first_name': 'John', 'last_name': 'Smith', 'grade': 12, 'fav_food': 'Pizza'}
>>> d["grade"] = 13
>>> d
{'first_name': 'John', 'last_name': 'Smith', 'grade': 13, 'fav_food': 'Pizza'}
>>> d.pop("fav_food")
'Pizza'
>>> d
{'first_name': 'John', 'last_name': 'Smith', 'grade': 13}
```

# Looping through dictionaries
```python
student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11
}

for key in student.keys():
    print(key)

print()
for val in student.values():
    print(val)

print()
for key, value in student.items():
    print(key, value)
```