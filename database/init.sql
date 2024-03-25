# This is an SQL initialization script. This script is executed once when the
# container is started for the first time. The purpose of this script is to
# create the database, define the tables/schema, and populate the tables with
# movie data.

#CREATE DATABASE imdb_database;
USE imdb_database;

CREATE TABLE names(
    name_id VARCHAR(500) PRIMARY KEY,
    `name` VARCHAR(4000),
    yearBorn YEAR(4),
    yearDied YEAR(4));

CREATE TABLE titles(
    title_id VARCHAR(500) PRIMARY KEY,
    title VARCHAR(4000),
    year YEAR(4),
    runtime INT,
    genre VARCHAR(1000));

CREATE TABLE roles(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_id VARCHAR(500),
    name_id VARCHAR(500),
    category VARCHAR(500),
    characters VARCHAR(8000),
    FOREIGN KEY(name_id) REFERENCES names(name_id),
    FOREIGN KEY(title_id) REFERENCES titles(title_id));

LOAD DATA LOCAL INFILE 
    'data/names.tsv' 
    INTO TABLE names
    FIELDS TERMINATED BY '\t' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS (
        `name_id`,
        `name`,
        `yearBorn`,
        `yearDied`);

LOAD DATA LOCAL INFILE 
    'data/titles.tsv' 
    INTO TABLE titles
    FIELDS TERMINATED BY '\t' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS (
        `title_id`,
        `title`,
        `year`,
        `runtime`,
        `genre`);

LOAD DATA LOCAL INFILE 
    'data/roles.tsv' 
    INTO TABLE roles
    FIELDS TERMINATED BY '\t' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS (
        `title_id`,
        `name_id`,
        `category`,
        `characters`);
