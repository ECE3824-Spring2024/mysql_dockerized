# Use the official MySQL image from Docker Hub (select version 5.7)
FROM mysql:5.7

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Copy SQL initialization script into the container
COPY ./init.sql /docker-entrypoint-initdb.d/

# Copy the data (tsv files) from local machine
COPY ./data /app/data

# Set working directory
WORKDIR /app
