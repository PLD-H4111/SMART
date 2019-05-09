
DROP TABLE IF EXISTS `Event` ;
DROP TABLE IF EXISTS `RestaurantAvailabilities` ;
DROP TABLE IF EXISTS `WaitingTime` ;
DROP TABLE IF EXISTS `Measure` ;
DROP TABLE IF EXISTS `Sensor` ;
DROP TABLE IF EXISTS `SensorType` ;
DROP TABLE IF EXISTS `Restaurant` ;
DROP TABLE IF EXISTS `Admin` ;

-- -----------------------------------------------------
-- Table `Restaurant`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `Restaurant` (
  `PK_idRestaurant` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  `theme` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`PK_idRestaurant`))
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `Event`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `Event` (
  `PK_idEvent` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  `beginningDate` DATE NOT NULL,
  `endingDate` DATE NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NULL,
  `eventDescription` TEXT NULL,
  PRIMARY KEY (`PK_idEvent`),
  INDEX `fk_restaurant_event_idx` (`FK_restaurant` ASC),
  CONSTRAINT `fk_restaurant_event`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `SensorType`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `SensorType` (
  `PK_idSensorType` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` TEXT NOT NULL,
  `unit` TEXT NOT NULL,
  PRIMARY KEY (`PK_idSensorType`))
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `Sensor`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `Sensor` (
  `PK_idSensor` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `position` INT(10) UNSIGNED NOT NULL,
  `name` TEXT NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NOT NULL,
  `FK_sensorType` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idSensor`),
  INDEX `FK_sensorRestaurant_idx` (`FK_restaurant` ASC),
  INDEX `FK_sensorType_idx` (`FK_sensorType` ASC),
  CONSTRAINT `FK_restaurant_sensor`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `Restaurant` (`PK_idRestaurant`)
    ON UPDATE CASCADE,
  CONSTRAINT `FK_sensorType`
    FOREIGN KEY (`FK_sensorType`)
    REFERENCES `SensorType` (`PK_idSensorType`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `Measure`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `Measure` (
  `PK_idMeasure` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `dateTime` DATETIME NOT NULL,
  `measure` DECIMAL(10,0) NOT NULL,
  `FK_sensor` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  INDEX `fk_Sensor_idx` (`FK_sensor` ASC),
  CONSTRAINT `fk_Sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `Sensor` (`PK_idSensor`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `RestaurantAvailabilities`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `RestaurantAvailabilities` (
  `PK_idRestaurantAvailabilities` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `openingTime` TIME NOT NULL,
  `closingTime` TIME NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idRestaurantAvailabilities`),
  INDEX `fk_Restaurant_idx` (`FK_restaurant` ASC),
  CONSTRAINT `fk_Restaurant_Availability`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `Restaurant` (`PK_idRestaurant`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `WaitingTime`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `WaitingTime` (
  `PK_idWaitingTime` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `waitingTime` INT(10) UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idWaitingTime`),
  INDEX `FK_restaurant_idx` (`FK_restaurant` ASC),
  CONSTRAINT `FK_restaurant_waitingTime`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `Restaurant` (`PK_idRestaurant`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `Admin`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `Admin` (
  `PK_idAdmin` INT NOT NULL AUTO_INCREMENT,
  `login` TEXT NOT NULL,
  `password` TEXT NOT NULL,
  PRIMARY KEY (`PK_idAdmin`))
ENGINE = InnoDB
AUTO_INCREMENT = 1;
