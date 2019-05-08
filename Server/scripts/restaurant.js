$(document).ready(function() {
    let now = new Date();
    let day = ("0" + now.getDate()).slice(-2);
    let month = ("0" + (now.getMonth() + 1)).slice(-2);
    let date = now.getFullYear() + "-" + month + "-" + day;
    $("#date-picker").val(date);
    update_page(new Date($("#date-picker").val()));
});

function update_page(date) {
    let restaurant = window.location.href.substr(window.location.href.indexOf('=') + 1)
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "get-restaurant-details",
            "restaurants": [restaurant],
            "date": date
        }),
        dataType: "json",
        success: function(data) {
            update_infos(data.restaurants[0]);
            update_chart(data.restaurants, date);
        }
    });
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "get-restaurant-events",
            "restaurant": restaurant,
            "date": date
        }),
        dataType: "json",
        success: function(data) {
            update_news(data.events);
        }
    });
}

function update_infos(data) {
    $("#restaurant-name").text(data.name);
    $("#restaurant-theme").text(data.theme);
    $("#restaurant-schedule").empty();
    data.schedule.forEach(function(time) {
        $("#restaurant-schedule").append(time + "<br/>");
    });
    $("#restaurant-status").html(create_status(data.status));
    $("#restaurant-current-waiting-time").text(create_eta(data.eta));
}

function update_news(events) {
    if(events.length < 1) {
        return;
    }
    let html = '<div class="col-lg-12">';
    events.forEach(function(item) {
        html += '<div class="card mt-2 mb-2 border-primary">';
        html += '<div class="card-header bg-primary text-white">' + item.name + ' (' + item.start + ' -> ' + item.end + ')</div>';
        html += '<div class="card-body">' + item.content + '</div>';
        html += '</div>';
    });
    html += '</div>';
    $("#events").html(html);
}

function calendar_handler() {
    update_page(new Date($("#date-picker").val()));
}

