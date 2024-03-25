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

ENTRYPOINT ["/bin/bash"]
