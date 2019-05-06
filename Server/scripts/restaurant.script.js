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
        data: {
            "action": "get-restaurant-details",
            "restaurants": [restaurant],
            "date": date
        },
        dataType: "json",
        success: function(data) {
            update_infos(data.restaurants[0]);
            update_chart(data.restaurants, date);
        }
    });
}

function update_infos(data) {
    $("#restaurant-name").html(data.name);
    $("#restaurant-theme").html(data.theme);
    $("#restaurant-schedule").html(data.schedule);
    $("#restaurant-status").html(data.status);
    $("#restaurant-throughput").html(data.throughput + "pers/min");
    $("#restaurant-current-waiting-time").html(data.eta + " min");
}

function calendar_handler() {
    update_page(new Date($("#date-picker").val()));
}

