#!/bin/bash
# arithmetic.sh
# This script performs basic arithmetic operations on two input numbers.

# Check if exactly two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 num1 num2"
    exit 1
fi

# Assign the arguments to variables
num1=$1
num2=$2

# Perform arithmetic operations
echo "Addition: $((num1 + num2))"
# $(( )) is used for arithmetic operations in Bash.

echo "Subtraction: $((num1 - num2))"
echo "Multiplication: $((num1 * num2))"
echo "Division: $((num1 / num2))"
# Note: Integer division only; use bc for floating-point division.

echo "Modulus: $((num1 % num2))"
echo "Exponentiation: $((num1 ** num2))"
# ** operator is used for exponentiation.
