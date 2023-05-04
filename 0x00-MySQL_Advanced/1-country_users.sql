-- first script for creating a table
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);