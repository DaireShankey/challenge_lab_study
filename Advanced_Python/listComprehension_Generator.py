# comprehensions_generators.py

# List comprehension: creating a list of squares
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# List comprehension with condition: squares of even numbers only
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# Generator expression: creates a generator object for memory efficiency
squares_gen = (x**2 for x in range(1, 11))
print("Generator squares:", list(squares_gen))  # Converting to list for display
