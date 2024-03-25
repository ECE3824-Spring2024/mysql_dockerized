# DOCKERFILE
#
# Image: Backend
#
# Purpose: Runs a Flask backend

# Use the official Python image from Docker Hub (select version 3.12).
FROM python:3.12

# Copy Flask source code into the image.
COPY . /app

# Set the current working directory.
WORKDIR /app

# Install Python dependencies for Flask and database access.
RUN pip install -r requirements.txt

# Set Flask environment variables.
ENV FLASK_APP backend.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

# Run the Flask backend.
CMD ["flask", "run"]
