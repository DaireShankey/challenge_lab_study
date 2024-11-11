# dictionary_operations.py

# Create a dictionary with some initial values
person = {"name": "Alice", "age": 25}

# Add a new key-value pair
person["city"] = "New York"
print("After adding city:", person)

# Update an existing key-value pair
person["age"] = 26
print("After updating age:", person)

# Iterate over key-value pairs
print("Person details:")
for key, value in person.items():
    print(key + ":", value)

# Access a specific value by key
print("Name:", person["name"])
