$(document).ready(function() {
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "get-all-restaurants-news"
        }),
        dataType: "json",
        success: function(data) {
            update_news(data.news);
        }
    });
});

function update_news(news) {
    $("#news-list").empty()
    for(var i=0; i<news.length; i++) {
        $("#news-list").append(
            "<tr>"
            + "<td>"
            +    "<a href='event_details.html?id=" + news[i].id +"'>" + news[i].title + "</a>"
            + "</td>"
            + "<td>" + news[i].start + "</td>"
            + "<td>" + news[i].end  + "</td>"
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

