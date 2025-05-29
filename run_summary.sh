#!/bin/bash
# run_summary.sh

echo "📦 Building Docker image..."
docker build -t soccer-summary .

echo "🚀 Running summary generator..."
docker run --rm --env-file .env soccer-summary
