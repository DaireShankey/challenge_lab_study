#!/bin/bash
# backup_script.sh - Backup a directory with a timestamp
source_dir="$1"
backup_dir="backups/$(basename $source_dir)_$(date +'%Y%m%d').tar.gz"
mkdir -p backups
tar -czf "$backup_dir" "$source_dir"

# Cron setup
# Add the following line to crontab by running `crontab -e`
# 0 1 * * * /path/to/backup_script.sh /path/to/source_dir
