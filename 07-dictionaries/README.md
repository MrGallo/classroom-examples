# Dictionaries Section Goals

- [Create, access, modify, insert, remove](#create-access-modify-insert-remove)
- [Loop over dictionary keys](#looping-through-dictionaries)
- [Loop over dictionary values](#looping-through-dictionaries)
- [Loop over dictionary values and keys](#looping-through-dictionaries)
- [Clear all values in a dictionary](#clear-all-values-in-a-dictionary)

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

# Clear all values in a dictionary
```python

```
