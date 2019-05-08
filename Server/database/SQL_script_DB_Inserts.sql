-- -----------------------------------------------------
-- Data for table `Restaurant`
-- -----------------------------------------------------
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'RI ligne de gauche', 'Restaurant self-service traditionnel');
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'RI ligne de droite', 'Restaurant self-service traditionnel');
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'RI ligne éco', 'Restaurant self-service traditionnel (ligne écologique)');
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Le Pied du Saule', 'Restaurant self-service du personnel');
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Le Prévert', 'Restauration rapide sur place ou à emporter');
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'L''Olivier', 'Restauration italienne');
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Le Grillon', 'Restaurant grill');


-- -----------------------------------------------------
-- Data for table `SensorType`
-- -----------------------------------------------------
INSERT INTO `SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Infrarouge', 'binary');
INSERT INTO `SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Ultrason', 'cm');


-- -----------------------------------------------------
-- Data for table `Sensor`
-- -----------------------------------------------------
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, "UR1", 1, 1);
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, "UR2", 1, 1);
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 2, "UL1", 1, 2);
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, "UR3", 2, 1);
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, "UR4", 2, 1);
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 2, "UL2", 2, 2);


-- -----------------------------------------------------
-- Data for table `Event`
-- -----------------------------------------------------
INSERT INTO `Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`, FK_restaurant, eventDescription) VALUES (DEFAULT, 'absence de certains membres', '2019-05-06', '2019-05-10', 1, 'Ils en ont marre de cuisiner');
INSERT INTO `Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`, FK_restaurant, eventDescription) VALUES (DEFAULT, 'absence de certains membres', '2019-05-06', '2019-05-10', 2, 'Ils en ont marre de cuisiner');


-- -----------------------------------------------------
-- Data for table `RestaurantAvailabilities`
-- -----------------------------------------------------
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '12:00:00', '13:30:00', 1);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '18:00:00', '23:50:00', 1);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '11:30:00', '13:30:00', 2);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-08', '18:00:00', '23:50:00', 2);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '07:00:00', '10:00:00', 1);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '12:00:00', '13:30:00', 1);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '07:30:00', '10:30:00', 2);
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-09', '11:30:00', '13:30:00', 2);


-- -----------------------------------------------------
-- Data for table `User`
-- -----------------------------------------------------
INSERT INTO `User` (`PK_idUser`, `identifiant`, `password`) VALUES (DEFAULT, "admin", "admin");
