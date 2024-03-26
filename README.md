# Nginx-Flask-MySQL Docker Project
The purpose of this project is to deploy a full-stack web app using Docker.
The app consists of three services, each of which is Dockerized:
- Database (MySQL)
- Backend (Flask)
- Frontend (Nginx/Javascript/HTML)
# Building and Deploying with Docker
First, clone this repository onto your local machine.
To start the application, use `docker-compose`:
```
docker-compose up -d --build
```
To stop and remove the containers, specify `down`:
```
docker-compose down
```
Please note that the **db_data** volume that is mounted to the MySQL container allows the database to persist if the container is stopped.
The presence of this volume prevents the `init.sql` script from re-initializing the database. Thus, if the database becomes corrupted, try
deleting this volume:
```
docker volume rm mysql_dockerized_db-data
```
Then re-compose (building is not necessary if you built the images before):
```
docker-compose up -d
```
