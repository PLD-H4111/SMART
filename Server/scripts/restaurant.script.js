$(document).ready(function() {
    
    
    var restaurant = window.location.href.substr(window.location.href.indexOf('=') + 1)
    $.ajax({
        url: "client",
        data: {
            action: "get-restaurants-details",
            id: restaurant
        },
        success: function(data) {
            $("#restaurant-name").html(data.name)
            $("#restaurant-theme").html(data.theme)
            $("#restaurant-schedule").html(data.schedule)
            $("#restaurant-status").html(data.status)
            $("#restaurant-throughput").html(data.throughput)
            $("#restaurant-current-waiting-time").html(data.eta)
        }
    })
})

