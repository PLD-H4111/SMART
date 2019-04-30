$(document).ready(function() {
    $.ajax({
        url: "/action_servlet",
        data: {"action": "get-restaurants-list"},
        dataType: "json",
        success: function(data) {
            $("#restaurants-list").empty()
            restaurants = data["restaurants"]
            for(var i=0; i<restaurants.length; i++) {
                $("#restaurants-list").append("<tr href='restaurant.html?id=" + restaurants[i].id + "'>")
                $("#restaurants-list").append("<td>" + restaurants[i].name + "</td>")
                $("#restaurants-list").append("<td>" + restaurants[i].status + "</td>")
                $("#restaurants-list").append("<td>" + restaurants[i].eta + "</td>")
                $("#restaurants-list").append("</tr>")
            }
        }
    });
})
    
