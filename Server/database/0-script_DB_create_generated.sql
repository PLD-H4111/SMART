SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema main
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema main
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `main` ;
USE `main` ;

-- -----------------------------------------------------
-- Table `main`.`Restaurant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`Restaurant` (
  `PK_idRestaurant` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `theme` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`PK_idRestaurant`));


-- -----------------------------------------------------
-- Table `main`.`SensorType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`SensorType` (
  `PK_idSensorType` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PK_idSensorType`));


-- -----------------------------------------------------
-- Table `main`.`Sensor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`Sensor` (
  `PK_idSensor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `position` INT UNSIGNED NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  `FK_sensorType` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idSensor`),
  CONSTRAINT `FK_restaurant_sensor`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `FK_sensorType`
    FOREIGN KEY (`FK_sensorType`)
    REFERENCES `main`.`SensorType` (`PK_idSensorType`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `FK_sensorRestaurant_idx` ON `main`.`Sensor` (`FK_restaurant` ASC);

CREATE INDEX `FK_sensorType_idx` ON `main`.`Sensor` (`FK_sensorType` ASC);


-- -----------------------------------------------------
-- Table `main`.`Measure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`Measure` (
  `PK_idMeasure` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dateTime` DATETIME NOT NULL,
  `measure` DECIMAL(10) NOT NULL,
  `FK_sensor` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  CONSTRAINT `fk_Sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `main`.`Sensor` (`PK_idSensor`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `fk_Sensor_idx` ON `main`.`Measure` (`FK_sensor` ASC);


-- -----------------------------------------------------
-- Table `main`.`Event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`Event` (
  `PK_idEvent` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `beginningDate` DATE NOT NULL,
  `endingDate` DATE NOT NULL,
  PRIMARY KEY (`PK_idEvent`));


-- -----------------------------------------------------
-- Table `main`.`WaitingTime`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`WaitingTime` (
  `PK_idWaitingTime` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `waitingTime` INT UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idWaitingTime`),
  CONSTRAINT `FK_restaurant_waitingTime`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `FK_restaurant_idx` ON `main`.`WaitingTime` (`FK_restaurant` ASC);


-- -----------------------------------------------------
-- Table `main`.`RestaurantAvailabilities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `main`.`RestaurantAvailabilities` (
  `PK_idRestaurantAvailabilities` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `openingTime` DATETIME NOT NULL,
  `closingTime` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idRestaurantAvailabilities`),
  CONSTRAINT `fk_Restaurant_Availability`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `fk_Restaurant_idx` ON `main`.`RestaurantAvailabilities` (`FK_restaurant` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

