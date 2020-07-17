-- prepares a MySQL server for the project
-- GRANT USAGE ON *.* TO 'nope_dev'@'localhost';

CREATE DATABASE IF NOT EXISTS nope_test_db;
CREATE USER IF NOT EXISTS nope_test@localhost IDENTIFIED BY 'nope_test_pwd';
USE nope_test_db;
GRANT ALL PRIVILEGES ON nope_test_db.* TO 'nope_test'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'nope_test'@'localhost';
FLUSH PRIVILEGES;
