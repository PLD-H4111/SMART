CREATE TABLE IF NOT EXISTS `mydb`.`Event` (
  `PK_idEvent` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `beginningDate` DATE NOT NULL,
  `endingDate` DATE NOT NULL,
  PRIMARY KEY (`PK_idEvent`))
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`SensorType` (
  `PK_idSensorType` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PK_idSensorType`))
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Restaurant` (
  `PK_idRestaurant` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `theme` VARCHAR(45) NULL,
  PRIMARY KEY (`PK_idRestaurant`))
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Sensor` (
  `PK_idSensor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `position` INT UNSIGNED NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  `FK_sensorType` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idSensor`),
  INDEX `FK_sensorRestaurant_idx` (`FK_restaurant` ASC),
  INDEX `FK_sensorType_idx` (`FK_sensorType` ASC),
  CONSTRAINT `FK_restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `mydb`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `FK_sensorType`
    FOREIGN KEY (`FK_sensorType`)
    REFERENCES `mydb`.`SensorType` (`PK_idSensorType`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Measure` (
  `PK_idMeasure` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dateTime` DATETIME NOT NULL,
  `measure` DECIMAL(10) NOT NULL,
  `FK_sensor` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  INDEX `FK_sensor_idx` (`FK_sensor` ASC),
  CONSTRAINT `FK_sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `mydb`.`Sensor` (`PK_idSensor`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`WaitingTime` (
  `PK_idWaitingTime` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `waitingTime` INT UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idWaitingTime`),
  INDEX `FK_restaurant_idx` (`FK_restaurant` ASC),
  CONSTRAINT `FK_restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `mydb`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`RestaurantAvailabilities` (
  `PK_idRestaurantAvailabilities` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `openingTime` DATETIME NOT NULL,
  `closingTime` DATETIME NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idRestaurantAvailabilities`),
  INDEX `fk_Restaurant_idx` (`FK_restaurant` ASC),
  CONSTRAINT `fk_Restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `mydb`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1

