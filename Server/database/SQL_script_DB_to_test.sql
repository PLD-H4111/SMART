-- MySQL Script generated by MySQL Workbench
-- ven. 03 mai 2019 08:57:25 CEST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema main
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema main
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `main` DEFAULT CHARACTER SET utf8 ;
USE `main` ;

-- -----------------------------------------------------
-- Table `main`.`Restaurant`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`Restaurant` ;

CREATE TABLE IF NOT EXISTS `main`.`Restaurant` (
  `PK_idRestaurant` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `theme` VARCHAR(45) NULL,
  PRIMARY KEY (`PK_idRestaurant`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `main`.`SensorType`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`SensorType` ;

CREATE TABLE IF NOT EXISTS `main`.`SensorType` (
  `PK_idSensorType` INT UNSIGNED NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PK_idSensorType`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `main`.`Sensor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`Sensor` ;

CREATE TABLE IF NOT EXISTS `main`.`Sensor` (
  `PK_idSensor` INT UNSIGNED NOT NULL,
  `position` INT UNSIGNED NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  `FK_sensorType` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idSensor`),
  CONSTRAINT `FK_restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `FK_sensorType`
    FOREIGN KEY (`FK_sensorType`)
    REFERENCES `main`.`SensorType` (`PK_idSensorType`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE INDEX `FK_sensorRestaurant_idx` ON `main`.`Sensor` (`FK_restaurant` ASC);

CREATE INDEX `FK_sensorType_idx` ON `main`.`Sensor` (`FK_sensorType` ASC);


-- -----------------------------------------------------
-- Table `main`.`Measure`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`Measure` ;

CREATE TABLE IF NOT EXISTS `main`.`Measure` (
  `PK_idMeasure` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dateTime` DATETIME NOT NULL,
  `measure` DECIMAL(10) NOT NULL,
  `FK_sensor` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  CONSTRAINT `FK_sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `main`.`Sensor` (`PK_idSensor`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;

CREATE INDEX `FK_sensor_idx` ON `main`.`Measure` (`FK_sensor` ASC);


-- -----------------------------------------------------
-- Table `main`.`Event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`Event` ;

CREATE TABLE IF NOT EXISTS `main`.`Event` (
  `PK_idEvent` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `beginningDate` DATE NOT NULL,
  `endingDate` DATE NOT NULL,
  PRIMARY KEY (`PK_idEvent`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `main`.`WaitingTime`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`WaitingTime` ;

CREATE TABLE IF NOT EXISTS `main`.`WaitingTime` (
  `PK_idWaitingTime` INT UNSIGNED NOT NULL,
  `waitingTime` INT UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idWaitingTime`),
  CONSTRAINT `FK_restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE INDEX `FK_restaurant_idx` ON `main`.`WaitingTime` (`FK_restaurant` ASC);


-- -----------------------------------------------------
-- Table `main`.`RestaurantAvailabilities`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`RestaurantAvailabilities` ;

CREATE TABLE IF NOT EXISTS `main`.`RestaurantAvailabilities` (
  `PK_idRestaurantAvailabilities` INT UNSIGNED NOT NULL,
  `date` DATE NOT NULL,
  `openingTime` TIME(0) NOT NULL,
  `closingTime` TIME(0) NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idRestaurantAvailabilities`),
  CONSTRAINT `fk_Restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;

CREATE INDEX `fk_Restaurant_idx` ON `main`.`RestaurantAvailabilities` (`FK_restaurant` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

