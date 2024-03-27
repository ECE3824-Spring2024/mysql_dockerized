# DOCKERFILE
#
# Image: Frontend
#
# Purpose: Runs a JS frontend

# Use the official nginx image from Docker Hub (select version 1.13).
FROM nginx:1.13-alpine

# Copy the configuration file.
COPY conf /etc/nginx/conf.d/default.conf

# Copy the static content files.
COPY html /var/www/html
