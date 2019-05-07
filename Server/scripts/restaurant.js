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
            "action": "get-restaurant-news",
            "restaurant": restaurant,
            "date": date
        }),
        dataType: "json",
        success: function(data) {
            update_news(data.news);
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

function update_news(news) {
    if(news.length < 1) {
        return;
    }
    let html = '<div class="col-lg-8">';
    news.forEach(function(item) {
        html += '<div class="panel panel-default panel-news">';
        html += '<div class="panel-heading">' + item.title + ' (' + item.start + ' -> ' + item.end + ')</div>';
        html += '<div class="panel-body">' + item.content + '</div>';
        html += '</div>';
    });
    html += '</div>';
    $("#news").html(html);
}

function calendar_handler() {
    update_page(new Date($("#date-picker").val()));
}

