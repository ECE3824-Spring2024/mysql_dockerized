# DOCKERFILE
#
# Image: MySQL
#
# Purpose: Dockerizes a MySQL database

# Use the official MySQL image from Docker Hub (select version 5.7).
FROM mysql:5.7

# Copy SQL initialization script into the container.
# This script is only run once to initialize the database,
# and is not run if a database volume is mounted. 
COPY ./init.sql /docker-entrypoint-initdb.d/

# Copy the data (tsv files) from local machine.
COPY ./data /app/data
