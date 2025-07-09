FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
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

# Expose port
EXPOSE 8000

# Create a startup script
RUN echo '#!/bin/bash\n\
python3 -c "\
from app import create_app, db;\
app = create_app();\
with app.app_context():\
    db.drop_all();\
    db.create_all()\
"\n\
gunicorn run:app --bind 0.0.0.0:$PORT' > /app/start.sh

RUN chmod +x /app/start.sh

# Run the application
CMD ["/app/start.sh"] 