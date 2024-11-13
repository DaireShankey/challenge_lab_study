#!/bin/bash
# process_manager.sh
# This script manages a specified process, allowing you to start, check, and stop it.

# Define the command for the process you want to manage (e.g., "sleep 300" as an example)
PROCESS_COMMAND="sleep 300"

# Define a file to store the process ID (PID) for easy reference
PID_FILE="process.pid"

# Function to start the process in the background
start_process() {
    # Check if the process is already running
    if [ -f "$PID_FILE" ]; then
        echo "Process is already running with PID $(cat $PID_FILE)."
    else
        # Start the process in the background and capture its PID
        $PROCESS_COMMAND &
        PROCESS_PID=$!

        # Save the PID to a file for tracking
        echo $PROCESS_PID > "$PID_FILE"
        echo "Process started with PID $PROCESS_PID."
    fi
}

# Function to check if the process is running
check_process() {
    if [ -f "$PID_FILE" ]; then
        PROCESS_PID=$(cat "$PID_FILE")
        
        # Check if the process is still active using kill -0
        if kill -0 "$PROCESS_PID" 2>/dev/null; then
            echo "Process is running with PID $PROCESS_PID."
        else
            echo "Process with PID $PROCESS_PID is not running."
            # Clean up the PID file if the process is no longer active
            rm -f "$PID_FILE"
        fi
    else
        echo "No process is currently running."
    fi
}

# Function to stop the process
stop_process() {
    if [ -f "$PID_FILE" ]; then
        PROCESS_PID=$(cat "$PID_FILE")

        # Terminate the process
        kill "$PROCESS_PID"
        echo "Process with PID $PROCESS_PID has been stopped."

        # Remove the PID file as the process is no longer running
        rm -f "$PID_FILE"
    else
        echo "No process to stop."
    fi
}

# Main script logic to handle user commands
echo "Process Manager: Please choose an option:"
echo "1. Start Process"
echo "2. Check Process"
echo "3. Stop Process"
read -p "Enter your choice (1/2/3): " choice

case $choice in
    1)
        start_process
        ;;
    2)
        check_process
        ;;
    3)
        stop_process
        ;;
    *)
        echo "Invalid choice. Please choose 1, 2, or 3."
        ;;
esac
