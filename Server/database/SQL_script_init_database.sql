
-- -----------------------------------------------------
-- Data for table `Restaurant`
-- -----------------------------------------------------
INSERT INTO `Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES 
    (DEFAULT, 'RI ligne de gauche', 'Restaurant self-service traditionnel'),
    (DEFAULT, 'RI ligne de droite', 'Restaurant self-service traditionnel'),
    (DEFAULT, 'RI ligne éco', 'Restaurant self-service traditionnel (ligne écologique)'),
    (DEFAULT, 'Le Pied du Saule', 'Restaurant self-service du personnel'),
    (DEFAULT, 'Le Prévert', 'Restauration rapide sur place ou à emporter'),
    (DEFAULT, 'L''Olivier', 'Restauration italienne'),
    (DEFAULT, 'Le Grillon', 'Restaurant grill'),
    (DEFAULT, 'Salle 2019', 'Les bonnes pizzas d\'INSAlgo');


-- -----------------------------------------------------
-- Data for table `SensorType`
-- -----------------------------------------------------
INSERT INTO `SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES 
    (DEFAULT, 'Infrarouge', 'binary'), 
    (DEFAULT, 'Ultrason', 'cm');


-- -----------------------------------------------------
-- Data for table `Sensor`
-- -----------------------------------------------------
INSERT INTO `Sensor` (`PK_idSensor`, `position`, `name`, `FK_restaurant`, `FK_sensorType`) VALUES
    (DEFAULT, 0, "UR1", 1, 1),
    (DEFAULT, 1, "UR2", 1, 1),
    (DEFAULT, 2, "UL1", 1, 2),
    (DEFAULT, 0, "UR3", 2, 1),
    (DEFAULT, 1, "UR4", 2, 1),
    (DEFAULT, 2, "UL2", 2, 2);


-- -----------------------------------------------------
-- Data for table `Event`
-- -----------------------------------------------------
INSERT INTO `Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`, FK_restaurant, eventDescription) VALUES 
    (DEFAULT, 'absence de certains membres', '2019-05-06', '2019-05-10', 1, 'Ils en ont marre de cuisiner'),
    (DEFAULT, 'absence de certains membres', '2019-05-06', '2019-05-10', 2, 'Ils en ont marre de cuisiner');


-- -----------------------------------------------------
-- Data for table `RestaurantAvailabilities`
-- -----------------------------------------------------
INSERT INTO `RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES 
    (DEFAULT, '2019-05-08', '12:00:00', '13:30:00', 1),
    (DEFAULT, '2019-05-08', '18:00:00', '23:50:00', 1),
    (DEFAULT, '2019-05-08', '11:30:00', '13:30:00', 2),
    (DEFAULT, '2019-05-08', '18:00:00', '23:50:00', 2),
    (DEFAULT, '2019-05-09', '07:00:00', '10:00:00', 1),
    (DEFAULT, '2019-05-09', '12:00:00', '13:30:00', 1),
    (DEFAULT, '2019-05-09', '07:30:00', '10:30:00', 2),
    (DEFAULT, '2019-05-09', '11:30:00', '13:30:00', 2);


-- -----------------------------------------------------
-- Data for table `Admin`
-- -----------------------------------------------------
INSERT INTO `Admin` (`PK_idAdmin`, `login`, `password`) VALUES 
    (DEFAULT, "admin", "admin");



INSERT INTO `WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES 
    (DEFAULT, 453, '2019-05-08 23:50:00', 1);
    
