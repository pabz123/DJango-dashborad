# Base image - Python 3.11 on slim Debian
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies first (separate layer for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "mysite.wsgi", "--bind", "0.0.0.0:8000", "--log-file", "-"]