$(document).ready(function() {
    let id = window.location.href.substr(window.location.href.indexOf('=') + 1)
    $.ajax({
        url: "/action_servlet",
        data: {
            "action": "get-event-details",
            "event": id
        },
        dataType: "json",
        success: function(data) {
            update_event(data.event);
        }
    });
});

function update_event(event) {
    $("#event-title").html(event.title);
    $("#event-content").html(event.content);
    $("#event-start-date").html(event.start);
    $("#event-end-date").html(event.end);
    event.restaurants.forEach(function(name) {
        $("#event-restaurants").append("<tr><td>" + name + "</td></tr>");
    });
}

