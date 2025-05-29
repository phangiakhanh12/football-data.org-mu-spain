# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY src/ ./src
RUN mkdir -p ./summaries
COPY tests/ ./tests

# Set environment variable for API token (can be overridden during docker run)
ENV API_TOKEN=your_default_token

# Run tests
# RUN pytest tests/   <-- Uncomment later after stabilizing

# Default command
CMD ["python", "src/crawl_soccer_data.py"]
