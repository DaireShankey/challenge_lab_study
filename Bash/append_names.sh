#!/bin/bash
# append_names.sh
# This script appends user input to a file until "quit" is typed.

# File to store names
filename="names.txt"

# Loop until "quit" is entered
while true; do
    # Prompt the user
    read -p "Enter a name (or type 'quit' to exit): " name
    # Exit loop if the user types 'quit'
    if [ "$name" == "quit" ]; then
        break
    fi
    # Append the name to the file
    echo "$name" >> "$filename"
done

echo "Names saved to $filename"
