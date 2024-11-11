# lambda_map_filter_reduce.py
from functools import reduce

# Lambda function to add two numbers
add = lambda x, y: x + y
print("Add 5 and 3:", add(5, 3))

# Using map to apply a function to all items in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Using filter to select items that meet a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Using reduce to apply a rolling computation to a list (sum all items)
total_sum = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total_sum)
