# file_handling.py

# Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Writing to a file in Python.")
# `with open` opens the file and ensures it’s closed automatically after writing.

# Read from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
# `file.read()` reads the entire file content as a single string.
