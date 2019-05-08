
DROP TABLE IF EXISTS `sql7290893`.`Event` ;
DROP TABLE IF EXISTS `sql7290893`.`RestaurantAvailabilities` ;
DROP TABLE IF EXISTS `sql7290893`.`WaitingTime` ;
DROP TABLE IF EXISTS `sql7290893`.`Measure` ;
DROP TABLE IF EXISTS `sql7290893`.`Sensor` ;
DROP TABLE IF EXISTS `sql7290893`.`SensorType` ;
DROP TABLE IF EXISTS `sql7290893`.`Restaurant` ;
DROP TABLE IF EXISTS `sql7290893`.`User` ;

-- -----------------------------------------------------
-- Table `sql7290893`.`Restaurant`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`Restaurant` (
  `PK_idRestaurant` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `theme` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`PK_idRestaurant`))
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`Event`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`Event` (
  `PK_idEvent` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `beginningDate` DATE NOT NULL,
  `endingDate` DATE NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NULL,
  `eventDescription` VARCHAR(200) NULL,
  PRIMARY KEY (`PK_idEvent`),
  INDEX `fk_restaurant_event_idx` (`FK_restaurant` ASC),
  CONSTRAINT `fk_restaurant_event`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `sql7290893`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`SensorType`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`SensorType` (
  `PK_idSensorType` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PK_idSensorType`))
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`Sensor`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`Sensor` (
  `PK_idSensor` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `position` INT(10) UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NOT NULL,
  `FK_sensorType` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idSensor`),
  INDEX `FK_sensorRestaurant_idx` (`FK_restaurant` ASC),
  INDEX `FK_sensorType_idx` (`FK_sensorType` ASC),
  CONSTRAINT `FK_restaurant_sensor`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `sql7290893`.`Restaurant` (`PK_idRestaurant`)
    ON UPDATE CASCADE,
  CONSTRAINT `FK_sensorType`
    FOREIGN KEY (`FK_sensorType`)
    REFERENCES `sql7290893`.`SensorType` (`PK_idSensorType`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`Measure`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`Measure` (
  `PK_idMeasure` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `dateTime` DATETIME NOT NULL,
  `measure` DECIMAL(10,0) NOT NULL,
  `FK_sensor` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  INDEX `fk_Sensor_idx` (`FK_sensor` ASC),
  CONSTRAINT `fk_Sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `sql7290893`.`Sensor` (`PK_idSensor`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`RestaurantAvailabilities`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`RestaurantAvailabilities` (
  `PK_idRestaurantAvailabilities` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `openingTime` TIME NOT NULL,
  `closingTime` TIME NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idRestaurantAvailabilities`),
  INDEX `fk_Restaurant_idx` (`FK_restaurant` ASC),
  CONSTRAINT `fk_Restaurant_Availability`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `sql7290893`.`Restaurant` (`PK_idRestaurant`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`WaitingTime`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`WaitingTime` (
  `PK_idWaitingTime` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `waitingTime` INT(10) UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_restaurant` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idWaitingTime`),
  INDEX `FK_restaurant_idx` (`FK_restaurant` ASC),
  CONSTRAINT `FK_restaurant_waitingTime`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `sql7290893`.`Restaurant` (`PK_idRestaurant`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1;


-- -----------------------------------------------------
-- Table `sql7290893`.`User`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `sql7290893`.`User` (
  `PK_idUser` INT NOT NULL AUTO_INCREMENT,
  `identifiant` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PK_idUser`))
ENGINE = InnoDB
AUTO_INCREMENT = 1;
