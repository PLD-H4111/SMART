var restaurant_checkboxes = [];

$(document).ready(function() {
    Notification.requestPermission(function(status) {
        if(Notification.permission !== status) {
            Notification.permission = status;
        }
    });

    restaurant_checkboxes = [];
    $.ajax({
        url: "action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            action: "get-restaurants-list"
        }),
        dataType: "json",
        success: function(data) {
            $("#restaurants-list").empty()
            var restaurants = data.restaurants
            for(var i=0; i<restaurants.length; i++) {
                $("#restaurants-list").append(
                    "<tr>"
                    + "<td>"
                    +   "<input type='checkbox' id='check" + restaurants[i].id + "' onchange='checkbox_handler();' checked/>"
                    +   "<label for='check" + restaurants[i].id + "'><a href='restaurant.html?id=" + restaurants[i].id + "'>" + restaurants[i].name + "</a></label>"
                    + "</td>"
                    + "<td>" + create_status(restaurants[i].status) + "</td>"
                    + "<td>" + create_eta(restaurants[i].eta) + "</td>"
                    + "</tr>"
                );
                restaurant_checkboxes.push(restaurants[i].id);
            }
            update();
        }
    });
})

function update() {
    var restaurant_ids = [];
    restaurant_checkboxes.forEach(function(id) {
        if($("#check" + id).is(':checked')) {
            restaurant_ids.push(id);
        }
    });

    $.ajax({
        url: "action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "get-restaurant-details",
            "restaurants": restaurant_ids,
            "date": new Date()
        }),
        dataType: "json",
        success: function(data) {
            update_chart(data.restaurants, new Date());
        }
    });
}

function checkbox_handler() {
    update();
}

