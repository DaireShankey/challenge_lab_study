#!/bin/bash
# monitor_process.sh
# This script checks if a given process (by PID) is still running.

# Ensure a PID is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <process_id>"
    exit 1
fi

process_id=$1

# Loop until the process is no longer running
while kill -0 $process_id 2>/dev/null; do
    # kill -0 checks if the process exists without terminating it.
    echo "Process $process_id is still running"
    sleep 5  # Wait 5 seconds before checking again
done

echo "Process $process_id has stopped"
