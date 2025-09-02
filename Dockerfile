# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend files
COPY backend/ /app/backend/
COPY db/schema.sql /app/db/schema.sql

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Set environment variables (update as needed)
ENV FLASK_APP=/app/backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port
EXPOSE 5000

# Initialize DB (optional: you may run this separately)
# RUN python /app/backend/sample_data.py

# Start Flask
CMD ["flask", "run"]
