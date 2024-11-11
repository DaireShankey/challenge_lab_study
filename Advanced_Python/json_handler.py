# json_handling.py
import json

# Define a Python dictionary to convert to JSON
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "Literature"]
}

# Write dictionary to JSON file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)
# `indent=4` formats the JSON output to be more readable.

# Read JSON data from a file
with open("person.json", "r") as file:
    data = json.load(file)
    print("Data read from JSON file:", data)
