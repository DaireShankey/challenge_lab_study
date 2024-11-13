#!/bin/bash
# Find the 5 largest files and save output to largest_files.txt
find . -type f -exec du -h {} + | sort -rh | head -n 5 > largest_files.txt
