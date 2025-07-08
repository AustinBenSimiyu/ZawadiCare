FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy the rest of the application
COPY . .

# Create uploads directory
RUN mkdir -p app/static/uploads

# Set environment variables
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Initialize the database
RUN python3 init_db.py

# Expose port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:8000"]
