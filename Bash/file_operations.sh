#!/bin/bash
# file_operations.sh
# This script demonstrates basic file operations and redirection.

# Step 1: Create a directory named 'sample_dir' if it doesn't exist
mkdir -p sample_dir
# -p flag ensures no error if directory exists and creates parent directories if necessary.

# Step 2: Create empty text files inside the directory
touch sample_dir/file1.txt sample_dir/file2.txt
# `touch` is used to create empty files or update timestamps if the file exists.

# Step 3: List files in 'sample_dir' and redirect the output to 'file_list.txt'
ls sample_dir > file_list.txt
# `>` redirects the output of `ls` to 'file_list.txt', overwriting the file if it exists.

# Step 4: Append a message to 'file_list.txt'
echo "File list generated on $(date)" >> file_list.txt
# `>>` appends the output of `echo` to 'file_list.txt' without overwriting it.
# $(date) is a command substitution that inserts the current date and time.
