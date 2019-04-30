$(document).ready(function() {
    var restaurant = window.location.href.substr(window.location.href.indexOf('=') + 1)
    $.ajax({
        url: "/action_servlet",
        data: {"action": "get-restaurants-details",
               "id": restaurant},
        dataType: "json",
        success: function(data) {
            $("#restaurant-name").html(data.name)
            $("#restaurant-theme").html(data.theme)

        }
    })
})
    
