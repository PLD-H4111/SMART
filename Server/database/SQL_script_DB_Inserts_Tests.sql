INSERT INTO `mydb`.`SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Infrarouge', 'binary');
INSERT INTO `mydb`.`SensorType` (`PK_idSensorType`, `type`, `unit`) VALUES (DEFAULT, 'Ultrason', 'cm');

INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'BeurkLigneGauche', 'beurk');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'BeurkLigneDroite', 'beurk');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'BeurkLigneCourte', 'beurk');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'PiedDuSaule', 'prof');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Prevert', 'fast food');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Olivier', 'italien');
INSERT INTO `mydb`.`Restaurant` (`PK_idRestaurant`, `name`, `theme`) VALUES (DEFAULT, 'Grillon', 'grillades grasses');

INSERT INTO `mydb`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 0, 1, 1);
INSERT INTO `mydb`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 1, 1, 1);
INSERT INTO `mydb`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 2, 1, 1);
INSERT INTO `mydb`.`Sensor` (`PK_idSensor`, `position`, `FK_restaurant`, `FK_sensorType`) VALUES (DEFAULT, 3, 1, 1);

INSERT INTO `mydb`.`Measure` (`PK_idMeasure`, `dateTime`, `measure`, `FK_sensor`) VALUES (DEFAULT, '2019-05-02 12:01:00', 1, 1);
INSERT INTO `mydb`.`Measure` (`PK_idMeasure`, `dateTime`, `measure`, `FK_sensor`) VALUES (DEFAULT, '2019-05-02 12:02:00', 0, 1);

INSERT INTO `mydb`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-02', '11:30:00', '13:30:00', 1);
INSERT INTO `mydb`.`RestaurantAvailabilities` (`PK_idRestaurantAvailabilities`, `date`, `openingTime`, `closingTime`, `FK_restaurant`) VALUES (DEFAULT, '2019-05-02', '11:30:00', '13:30:00', 2);

INSERT INTO `mydb`.`WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES (DEFAULT, 300, '2019-05-02 12:05:00', 1);
INSERT INTO `mydb`.`WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES (DEFAULT, 600, '2019-05-02 12:06:00', 1);
INSERT INTO `mydb`.`WaitingTime` (`PK_idWaitingTime`, `waitingTime`, `date`, `FK_restaurant`) VALUES (DEFAULT, 780, '2019-05-02 12:07:00', 1);

