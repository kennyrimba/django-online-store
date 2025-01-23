# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies for MySQL client and network debugging
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    python3-dev \
    build-base \
    pkgconfig \
    mysql-client \
    netcat-openbsd \
    git  # Added git installation here

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir \
        mysqlclient==2.2.0 \
        Django==4.2.5 \
        environs \
        Pillow==9.5.0 \
        django-extensions==3.2.3 \
        django-crispy-forms==2.0 \
        crispy-bootstrap4==2022.1 \
        django-allauth==0.57.0 \
        stripe==6.6.0 \
        django-guest-user==0.5.5

# Copy project
COPY app /app

# Expose port
EXPOSE 8000

# Create an entrypoint script for debugging and waiting for DB
RUN printf '#!/bin/sh\n\
echo "Waiting for MySQL to be ready..."\n\
while ! nc -z mysql-service 3306; do\n\
  echo "Waiting for database connection..."\n\
  sleep 5\n\
done\n\
echo "Database is up - executing commands"\n\
python manage.py migrate\n\
python manage.py loaddata dumped_data.json\n\
python manage.py runserver 0.0.0.0:8000\n' > /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh

# Default command
CMD ["/app/entrypoint.sh"]