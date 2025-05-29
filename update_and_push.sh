#!/bin/bash
cd /home/khanhphan/football-data.org-mu-spain || exit 1

# Now run your docker build and run commands here
docker build -t mu-summary .
docker run --rm mu-summary

# And your git add, commit, push steps
git add league_summary.txt
git commit -m "Weekly update: $(date '+%Y-%m-%d')"
git push
