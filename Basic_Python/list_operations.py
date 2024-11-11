# list_operations.py

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Append a new number to the list
numbers.append(6)
print("After appending 6:", numbers)

# Remove the first occurrence of 3 from the list
numbers.remove(3)
print("After removing 3:", numbers)

# Iterate through the list and print each element
print("List elements:")
for num in numbers:
    print(num)

# Access list elements by index
print("First element:", numbers[0])
print("Last element:", numbers[-1])
# `numbers[0]` is the first element, `numbers[-1]` is the last element.
