-- Prepares a MySQL server for the AirBnB Clone - MySQL Project

-- Creates a the database "hbnb_dev_db"
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates a new user "hbnb_dev"
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges for the user "hbnb_dev" on the database "hbnb_dev_db"
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grants "SELECT" privilege to "hbnb_dev" on the database "performance_schema"
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
