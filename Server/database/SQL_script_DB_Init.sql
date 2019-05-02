CREATE TABLE IF NOT EXISTS `mydb`.`Archive` (
  `PK_idArchive` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tempsAttente` INT UNSIGNED NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  `date` DATETIME NOT NULL,
  `FK_event` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idArchive`),
  INDEX `FK_restaurant_idx` (`FK_restaurant` ASC),
  INDEX `FK_event_idx` (`FK_event` ASC),
  CONSTRAINT `FK_restaurant`
    FOREIGN KEY (`FK_restaurant`)
    REFERENCES `mydb`.`Restaurant` (`PK_idRestaurant`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `FK_event`
    FOREIGN KEY (`FK_event`)
    REFERENCES `mydb`.`Event` (`PK_idEvent`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Event` (
  `PK_idEvent` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `event` VARCHAR(45) NOT NULL,
  `dateDebut` DATE NULL,
  `dateFin` DATE NULL,
  PRIMARY KEY (`PK_idEvent`))
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Measure` (
  `PK_idMeasure` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `time` TIMESTAMP(10) NOT NULL,
  `FK_sensor` INT UNSIGNED NOT NULL,
  `measure` DECIMAL(10) NOT NULL,
  PRIMARY KEY (`PK_idMeasure`),
  INDEX `FK_sensor_idx` (`FK_sensor` ASC),
  CONSTRAINT `FK_sensor`
    FOREIGN KEY (`FK_sensor`)
    REFERENCES `mydb`.`Sensor` (`PK_idSensor`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Restaurant` (
  `PK_idRestaurant` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PK_idRestaurant`))
ENGINE = ndbcluster
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`Sensor` (
  `PK_idSensor` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `FK_sensorType` INT UNSIGNED NOT NULL,
  `FK_restaurant` INT UNSIGNED NOT NULL,
  `FK_sensorPosition` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PK_idSensor`),
  INDEX `FK_sensorPosition_idx` (`FK_sensorPosition` ASC),
  INDEX `FK_sensorRestaurant_idx` (`FK_restaurant` ASC),
  INDEX `FK_sensorType_idx` (`FK_sensorType` ASC),
  CONSTRAINT `FK_sensorPosition`
    FOREIGN KEY (`FK_sensorPosition`)
    REFERENCES `mydb`.`SensorPosition` (`PK_idSensorPosition`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
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

CREATE TABLE IF NOT EXISTS `mydb`.`SensorPosition` (
  `PK_idSensorPosition` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `SensorPosition` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PK_idSensorPosition`))
ENGINE = InnoDB
AUTO_INCREMENT = 1

CREATE TABLE IF NOT EXISTS `mydb`.`SensorType` (
  `PK_idSensorType` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(45) NOT NULL,
  `unit` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`PK_idSensorType`))
ENGINE = InnoDB
AUTO_INCREMENT = 1

INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, 'rentrée scolaire', NULL, NULL);
INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, 'veille de vacances', NULL, NULL);
INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, 'vacances', NULL, NULL);
INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, 'période de partiels PC', NULL, NULL);
INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, 'effectif réduit', NULL, NULL);
INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, 'problème sur le système de détection', NULL, NULL);
INSERT INTO `mydb`.`Event` (`PK_idEvent`, `event`, `dateDebut`, `dateFin`) VALUES (DEFAULT, '24h INSA', NULL, NULL);

INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (, 'BeurkLigneGauche');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (, 'BeurkLigneDroite');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (DEFAULT, 'BeurkLigneCourte');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (DEFAULT, 'PiedDuSaule');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (DEFAULT, 'Prevert');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (DEFAULT, 'Olivier');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `description`) VALUES (DEFAULT, 'Grillon');

INSERT INTO `mydb`.`SensorPosition` (`PK_idSensorPosition`, `SensorPosition`) VALUES (DEFAULT, 'position1');
INSERT INTO `mydb`.`SensorPosition` (`PK_idSensorPosition`, `SensorPosition`) VALUES (DEFAULT, 'position2');
INSERT INTO `mydb`.`SensorPosition` (`PK_idSensorPosition`, `SensorPosition`) VALUES (DEFAULT, 'position3');
INSERT INTO `mydb`.`SensorPosition` (`PK_idSensorPosition`, `SensorPosition`) VALUES (DEFAULT, 'position4');
INSERT INTO `mydb`.`SensorPosition` (`PK_idSensorPosition`, `SensorPosition`) VALUES (DEFAULT, 'position5');

INSERT INTO `mydb`.`SensorType` (`PK_idSensorType`, `description`, `unit`) VALUES (DEFAULT, 'Infrarouge', 'binary');
INSERT INTO `mydb`.`SensorType` (`PK_idSensorType`, `description`, `unit`) VALUES (DEFAULT, 'Ultrason', 'cm');
INSERT INTO `mydb`.`SensorType` (`PK_idSensorType`, `description`, `unit`) VALUES (DEFAULT, 'Wifi', 'persons');
INSERT INTO `mydb`.`SensorType` (`PK_idSensorType`, `description`, `unit`) VALUES (DEFAULT, 'Borne', '?');

