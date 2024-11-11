#!/bin/bash
# disk_check.sh
# This script checks disk usage and sends an alert if it exceeds 80%.

# Set threshold
threshold=80

# Get disk usage percentage of the root directory
usage=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
# df / displays disk usage for root.
# grep / selects the line with the percentage.
# awk '{ print $5 }' selects the 5th column (percentage used).
# sed 's/%//g' removes the % symbol.

# Check if usage exceeds threshold
if [ "$usage" -gt "$threshold" ]; then
    echo "Alert: Disk usage is at ${usage}%"
else
    echo "Disk usage is at ${usage}%, which is within the safe limit."
fi
