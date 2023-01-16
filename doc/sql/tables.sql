-- Table user
CREATE TABLE IF NOT EXISTS `mydb_uat`.`user` (
  `user_id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(150) NOT NULL,
  `password` VARCHAR(128) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `first_name` VARCHAR(150) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `is_active` TINYINT NULL,
  `date_joined` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Table status
CREATE TABLE IF NOT EXISTS `mydb_uat`.`status` (
  `status_id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(32) NOT NULL,
  `label` VARCHAR(64) NOT NULL,
  `created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Table property
CREATE TABLE IF NOT EXISTS `mydb_uat`.`property` (
  `property_id` INT AUTO_INCREMENT,
  `address` VARCHAR(150) NOT NULL,
  `city` VARCHAR(90) NOT NULL,
  `price` BIGINT(20) NOT NULL,
  `description` TINYTEXT NULL,
  `year` INT(4) NOT NULL,
  `created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `update` DATETIME NOT NULL,
  `status_id` INT NOT NULL,
  PRIMARY KEY (`property_id`),
  FOREIGN KEY (`status_id`)
    REFERENCES `mydb_uat`.`status` (`status_id`)
    ON UPDATE RESTRICT ON DELETE CASCADE
);
-- Table like / rating
CREATE TABLE IF NOT EXISTS `mydb_uat`.`rating` (
  `rating_id` INT AUTO_INCREMENT,
  `property_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `score` INT(4) NOT NULL,
  `message` TINYTEXT NOT NULL,
  `created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`rating_id`),
  FOREIGN KEY (`property_id`)
    REFERENCES `mydb_uat`.`property` (`property_id`)
    ON UPDATE RESTRICT ON DELETE CASCADE,
  FOREIGN KEY (`user_id`)
    REFERENCES `mydb_uat`.`user` (`user_id`)
    ON UPDATE RESTRICT ON DELETE CASCADE
);
