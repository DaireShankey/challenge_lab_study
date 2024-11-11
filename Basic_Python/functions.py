# functions.py

# Define a function to add two numbers
def add_numbers(a, b):
    result = a + b
    return result
# `a` and `b` are parameters, `result` is returned to the caller.

# Define a function to greet a person
def greet(name):
    print("Hello, " + name + "!")
# `name` is a parameter used in the greeting message.

# Call the functions
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)

greet("Alice")
