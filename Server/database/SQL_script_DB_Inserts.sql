-- -----------------------------------------------------
-- Data for table `sql7290893`.`Restaurant`
-- -----------------------------------------------------
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'RI ligne de gauche', 'le restaurant INSA');
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'RI ligne de droite', 'le restaurant INSA');
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'RI ligne courte', 'le restaurant INSA');
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Pied du Saule', 'restaurant pour les prof');
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Prevert', 'restauration rapide');
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Olivier', 'restaurant italien');
INSERT INTO `sql7290893`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Grillon', 'restaurant a base de grillades');


-- -----------------------------------------------------
-- Data for table `sql7290893`.`SensorType`
-- -----------------------------------------------------
INSERT INTO `sql7290893`.`SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Infrarouge', 'binary');
INSERT INTO `sql7290893`.`SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Ultrason', 'cm');


-- -----------------------------------------------------
-- Data for table `sql7290893`.`Sensor`
-- -----------------------------------------------------
INSERT INTO `sql7290893`.`Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, "UR1", 1, 1);
INSERT INTO `sql7290893`.`Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, "UR2", 1, 1);
INSERT INTO `sql7290893`.`Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 2, "UL1", 1, 2);
INSERT INTO `sql7290893`.`Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, "UR3", 2, 1);
INSERT INTO `sql7290893`.`Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, "UR4", 2, 1);
INSERT INTO `sql7290893`.`Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 2, "UL2", 2, 2);


-- -----------------------------------------------------
-- Data for table `sql7290893`.`Event`
-- -----------------------------------------------------
INSERT INTO `sql7290893`.`Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`, FK_restaurant, eventDescription) VALUES (DEFAULT, 'absence de certains membres', '2019-05-06', '2019-05-10', 1, 'Ils en ont marre de cuisiner');
INSERT INTO `sql7290893`.`Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`, FK_restaurant, eventDescription) VALUES (DEFAULT, 'absence de certains membres', '2019-05-06', '2019-05-10', 2, 'Ils en ont marre de cuisiner');


-- -----------------------------------------------------
-- Data for table `sql7290893`.`RestaurantAvailabilities`
-- -----------------------------------------------------
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '12:00:00', '13:30:00', 1);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '18:00:00', '23:50:00', 1);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '11:30:00', '13:30:00', 2);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '18:00:00', '23:50:00', 2);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '07:00:00', '10:00:00', 1);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '12:00:00', '13:30:00', 1);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '07:30:00', '10:30:00', 2);
INSERT INTO `sql7290893`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '11:30:00', '13:30:00', 2);


-- -----------------------------------------------------
-- Data for table `sql7290893`.`User`
-- -----------------------------------------------------
INSERT INTO `sql7290893`.`User` (`PK_idUser`, `identifiant`, `password`) VALUES (DEFAULT, "admin", "admin");