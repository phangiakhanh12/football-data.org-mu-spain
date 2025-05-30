#!/bin/bash
cd /home/khanhphan/football-data.org-mu-spain || exit 1

set -e  # Exit on error

echo "📦 Running container to fetch data..."
docker build -t league-summary .
docker run --env-file .env -v "$PWD:/app" league-summary

echo "✅ league_summary.txt generated."

# Git automation
echo "📤 Committing and pushing to GitHub..."
git add .
git commit -m "📊 Weekly update: $(date)"
git push origin main

echo "✅ All done!"
