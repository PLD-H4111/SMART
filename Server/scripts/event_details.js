$(document).ready(function() {
    let id = window.location.href.substr(window.location.href.indexOf('=') + 1)
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "get-event-details",
            "event": id
        }),
        dataType: "json",
        success: function(data) {
            update_event(data.event);
        }
    });
});

function update_event(event) {
    $("#event-title").text(event.name);
    $("#event-content").text(event.content);
    $("#event-start-date").text(event.start);
    $("#event-end-date").text(event.end);
    event.restaurants.forEach(function(name) {
        $("#event-restaurants").append("<tr><td>" + name + "</td></tr>");
    });
}

