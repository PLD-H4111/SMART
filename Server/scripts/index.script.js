$(document).ready(function() {
    $.ajax({
        url: "action_servlet",
        data: {
            "action": "get-restaurants-list"
        },
        dataType: "json",
        success: function(data) {
            $("#restaurants-list").empty()
            restaurants = data.restaurants
            for(var i=0; i<restaurants.length; i++) {
                $("#restaurants-list").append(
                    "<tr>"
                    + "<td><a href='restaurant.html?id=" + restaurants[i].id + "'>" + restaurants[i].name + "</a></td>"
                    + "<td>" + restaurants[i].status + "</td>"
                    + "<td>" + restaurants[i].eta + "</td>"
                    + "</tr>"
                );
            }
        }
    });
})

