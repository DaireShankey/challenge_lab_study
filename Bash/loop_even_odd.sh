#!/bin/bash
# loop_condition.sh
# This script checks if numbers from 1 to 10 are even or odd.

# Loop through numbers 1 to 10
for i in {1..10}; do
    # Check if the number is even using modulus
    if ((i % 2 == 0)); then
        echo "$i is even"
    else
        echo "$i is odd"
    fi
done
