-- -----------------------------------------------------
-- Data for table `main`.`Restaurant`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'BeurkLigneGauche', 'beurk');
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'BeurkLigneDroite', 'beurk');
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'BeurkLigneCourte', 'beurk');
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'PiedDuSaule', 'prof');
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Prevert', 'fast food');
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Olivier', 'italien');
INSERT INTO `main`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Grillon', 'grillades');

COMMIT;


-- -----------------------------------------------------
-- Data for table `main`.`SensorType`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Infrarouge', 'binary');
INSERT INTO `main`.`SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Ultrason', 'cm');

COMMIT;


-- -----------------------------------------------------
-- Data for table `main`.`Sensor`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, 1, 1);
INSERT INTO `main`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, 1, 1);
INSERT INTO `main`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 2, 1, 1);
INSERT INTO `main`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 3, 1, 1);
INSERT INTO `main`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, 2, 2);
INSERT INTO `main`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, 2, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `main`.`Measure`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`Measure` (`PK_idMeasure`, `dateTime`, `measure`, `FK_sensor`) VALUES (DEFAULT, '2019-05-02 12:01:00', 1, 1);
INSERT INTO `main`.`Measure` (`PK_idMeasure`, `dateTime`, `measure`, `FK_sensor`) VALUES (DEFAULT, '2019-05-02 12:02:00', 0, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `main`.`Event`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`) VALUES (DEFAULT, 'rentrée scolaire', '2019-05-05', '2019-05-05');
INSERT INTO `main`.`Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`) VALUES (DEFAULT, 'veille de vacances', '2019-09-21', '2019-09-21');

COMMIT;


-- -----------------------------------------------------
-- Data for table `main`.`WaitingTime`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES (DEFAULT, 300, '2019-05-02 12:05:00', 1);
INSERT INTO `main`.`WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES (DEFAULT, 600, '2019-05-02 12:06:00', 1);
INSERT INTO `main`.`WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES (DEFAULT, 780, '2019-05-02 12:07:00', 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `main`.`RestaurantAvailabilities`
-- -----------------------------------------------------
START TRANSACTION;
USE `main`;
INSERT INTO `main`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-02', '11:30:00', '13:30:00', 1);
INSERT INTO `main`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-02', '11:30:00', '13:30:00', 1);

COMMIT;


