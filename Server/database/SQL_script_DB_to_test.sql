-- -----------------------------------------------------
-- Clean de la DB`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `main`.`Restaurant` ;
DROP TABLE IF EXISTS `main`.`Measure` ;
DROP TABLE IF EXISTS `main`.`SensorType` ;
DROP TABLE IF EXISTS `main`.`Sensor` ;
DROP TABLE IF EXISTS `main`.`Event` ;
DROP TABLE IF EXISTS `main`.`WaitingTime` ;
DROP TABLE IF EXISTS `main`.`RestaurantAvailabilities` ;

-- -----------------------------------------------------
-- Table `main`.`Restaurant`
-- -----------------------------------------------------
CREATE TABLE `main`.`Restaurant` (
  `PK_idRestaurant` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `theme` VARCHAR(45) NULL,
  PRIMARY KEY (`PK_idRestaurant`));

-- -----------------------------------------------------
-- Table `main`.`SensorType`
-- -----------------------------------------------------
CREATE TABLE `main`.`SensorType` (
  `PK_idSensorType` INT UNSIGNED NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PK_idSensorType`));

-- -----------------------------------------------------
-- Table `main`.`Sensor`
-- -----------------------------------------------------
CREATE TABLE `main`.`Sensor` (
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
    ON UPDATE CASCADE);

CREATE INDEX `FK_sensorRestaurant_idx` ON `main`.`Sensor` (`FK_restaurant` ASC);

CREATE INDEX `FK_sensorType_idx` ON `main`.`Sensor` (`FK_sensorType` ASC);

-- -----------------------------------------------------
-- Table `main`.`Measure`
-- -----------------------------------------------------
CREATE TABLE `main`.`Measure` (
  `PK_idMeasure` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dateTime` DATETIME NOT NULL,
  `measure` DECIMAL(10) NOT NULL,
  `FK_sensor` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  CONSTRAINT `FK_sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `main`.`Sensor` (`PK_idSensor`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `FK_sensor_idx` ON `main`.`Measure` (`FK_sensor` ASC);

-- -----------------------------------------------------
-- Table `main`.`Event`
-- -----------------------------------------------------
CREATE TABLE `main`.`Event` (
  `PK_idEvent` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `beginningDate` DATE NOT NULL,
  `endingDate` DATE NOT NULL,
  PRIMARY KEY (`PK_idEvent`));

-- -----------------------------------------------------
-- Table `main`.`WaitingTime`
-- -----------------------------------------------------
CREATE TABLE `main`.`WaitingTime` (
  `PK_idWaitingTime` INT UNSIGNED NOT NULL,
  `waitingTime` INT UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idWaitingTime`),
  CONSTRAINT `FK_restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `FK_restaurant_idx` ON `main`.`WaitingTime` (`FK_restaurant` ASC);

-- -----------------------------------------------------
-- Table `main`.`RestaurantAvailabilities`
-- -----------------------------------------------------
CREATE TABLE `main`.`RestaurantAvailabilities` (
  `PK_idRestaurantAvailabilities` INT UNSIGNED NOT NULL,
  `openingTime` DATETIME NOT NULL,
  `closingTime` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idRestaurantAvailabilities`),
  CONSTRAINT `fk_Restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `main`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

CREATE INDEX `fk_Restaurant_idx` ON `main`.`RestaurantAvailabilities` (`FK_restaurant` ASC);

