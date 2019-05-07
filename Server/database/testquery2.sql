SELECT name, theme, status, eta
FROM restaurantAvailabilities, 
	(SELECT PK_idRestaurant, name, theme, "1" AS status, eta
	FROM restaurant, restaurantAvailabilities, waitingTime, 
		(SELECT o.waitingTime as eta, name as nom
		FROM restaurant, waitingtime o LEFT JOIN waitingtime b
			ON o.FK_restaurant = b.FK_restaurant AND o.date < b.date
		WHERE PK_idRestaurant = o.FK_restaurant
		AND b.date is NULL
		)o
	WHERE PK_idRestaurant = restaurantAvailabilities.FK_restaurant
	AND nom = name
	AND PK_idRestaurant = waitingtime.FK_restaurant
	AND restaurantAvailabilities.date = date(NOW())
	AND openingTime < time(NOW())
	AND closingTime > time(NOW())
	UNION
	SELECT PK_idRestaurant, name, theme, "0" AS status, w AS eta
FROM restaurant, 
		(SELECT o.waitingTime as w, name as nom
		FROM restaurant, waitingtime o LEFT JOIN waitingtime b
			ON o.FK_restaurant = b.FK_restaurant AND o.date < b.date
		WHERE PK_idRestaurant = o.FK_restaurant
		AND b.date is NULL
		)o
	WHERE nom = name
	AND name NOT IN (
		SELECT name FROM restaurant, restaurantAvailabilities
		WHERE PK_idRestaurant = FK_restaurant
		AND restaurantAvailabilities.date = date(NOW())
		AND openingTime < time(NOW())
		AND closingTime > time(NOW())
	))eta
WHERE restaurantAvailabilities.FK_restaurant = PK_idRestaurant
AND PK_idRestaurant = 1
AND date(restaurantAvailabilities.date) = date(NOW());