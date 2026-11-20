#!/bin/bash
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
tar -czf backup_storage/backup_$TIMESTAMP.tar.gz -C primary_data .
cp primary_data/index.html backup_storage/index.html
echo "[SUCCESS] Backup created at $TIMESTAMP"
