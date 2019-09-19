import json


data = {
    "students": [
        {"first_name": "John"},
        {"first_name": "Sally"}
    ],
    "classrooms": {
        0: {"course_code": "ICS4U"}
    }
}

data["students"].append({"first_name": "Frank"})

with open('markbook.json', "w") as f:
    json.dump(data, f)
