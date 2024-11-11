#!/bin/bash
# menu.sh
# This script provides a menu for the user to select an action.

while true; do
    echo "Choose an option:"
    echo "1. Display date"
    echo "2. List files in current directory"
    echo "3. Check disk usage"
    echo "4. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)  # Display current date and time
            echo "Current date and time: $(date)"
            ;;
        2)  # List files in current directory
            echo "Files in $(pwd):"
            ls
            ;;
        3)  # Check disk usage
            df -h
            ;;
        4)  # Exit the program
            echo "Exiting..."
            break
            ;;
        *)  # Handle invalid input
            echo "Invalid choice. Please select an option from 1 to 4."
            ;;
    esac
done
