-- This SQL script create a table `users` with the following requirements:
-- Attributes:
--      id - integer, never null, auto increment, primary key
--      email - string (255 characters), never null, unique
--      name - string (255 characters)

-- Creates the `users` table with all attributes.
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255),
    PRIMARY KEY (`id`),
    UNIQUE KEY email_unique (`email`)
)
