$(document).ready(function() {
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "get-all-restaurants-events"
        }),
        dataType: "json",
        success: function(data) {
            update_news(data.events);
        }
    });
});

function update_news(events) {
    $("#events-list").empty()
    for(var i=0; i<events.length; i++) {
        $("#events-list").append(
            "<tr>"
            + "<td>"
            +    "<a href='event_details.html?id=" + events[i].id +"'>" + events[i].name + "</a>"
            + "</td>"
            + "<td>" + events[i].start + "</td>"
            + "<td>" + events[i].end  + "</td>"
            + "</tr>"
        );
    }
}

function logout() {
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "admin-logout"
        })
    });
    redirect("index.html");
}

