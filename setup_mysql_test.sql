-- Prepares a MYSQL server for the "AirBnB_Clone - MySQL" project

-- Creates a the database "hbnb_test_db"
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a new user "hbnb_test"
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges for the user "hbnb_test" on the database "hbnb_test_db"
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants "SELECT" privilege to "hbnb_test" on the database "performance_schema"
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
