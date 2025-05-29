#!/bin/bash
set -e

echo "Starting soccer data crawler..."

python3 src/crawl_soccer_data.py --output-dir "$SUMMARY_DIR"

echo "Crawler finished."
