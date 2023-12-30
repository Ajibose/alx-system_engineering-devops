-- Create database and table
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6
(
	id	INT NOT NULL AUTO_INCREMENT,
	name	VARCHAR(150) NOT NULL,
	PRIMARY KEY (id)
);
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
INSERT INTO nexus6 ( name ) VALUES ('Leon');
