#!/bin/bash
# search_keyword.sh
# This script searches for a keyword in a file and displays matching lines with line numbers.

# Check if both a keyword and a filename are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <keyword> <file>"
    exit 1
fi

keyword=$1
file=$2

# Use grep to search for the keyword in the file
grep -n "$keyword" "$file"
# -n option shows line numbers.
# "$keyword" and "$file" are quoted to handle spaces in the arguments.
