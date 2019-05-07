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
        data: {
            "action": "get-restaurants-list"
        },
        dataType: "json",
        success: function(data) {
            $("#restaurants-list").empty()
            var restaurants = data.restaurants
            for(var i=0; i<restaurants.length; i++) {
                $("#restaurants-list").append(
                    "<tr>"
                    + "<td>"
                    +   "<input type='checkbox' id='check" + restaurants[i].id + "' onchange='checkbox_handler();' checked/>"
                    +   "<a href='restaurant.html?id=" + restaurants[i].id + "'>" + restaurants[i].name + "</a>"
                    + "</td>"
                    + "<td>" + create_status(restaurants[i].status) + "</td>"
                    + "<td>" + restaurants[i].eta + " min</td>"
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
        data: {
            "action": "get-restaurant-details",
            "restaurants": restaurant_ids,
            "date": 0
        },
        dataType: "json",
        success: function(data) {
            update_chart(data.restaurants, new Date());
        }
    });
}

function checkbox_handler() {
    update();
}

function create_status(status) {
    if(status === "open") {
        return "<span class='status_open'>OUVERT</span>";
    }
    if(status === "closed") {
        return "<span class='status_closed'>FERME</span>";
    }
}

