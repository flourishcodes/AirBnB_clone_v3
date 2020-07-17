-- prepares a MySQL server for the project
-- GRANT USAGE ON *.* TO 'nope_dev'@'localhost';

CREATE DATABASE IF NOT EXISTS nope_dev_db;
CREATE USER IF NOT EXISTS nope_dev@localhost IDENTIFIED BY 'nope_dev_pwd';
USE nope_dev_db;
GRANT ALL PRIVILEGES ON nope_dev_db.* TO 'nope_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'nope_dev'@'localhost';
FLUSH PRIVILEGES;
