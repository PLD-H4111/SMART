var restaurant_checkboxes = [];

$(document).ready(function() {
    restaurant_checkboxes = [];
    $.ajax({
        url: "action_servlet",
        data: {
            "action": "get-restaurants-list"
        },
        dataType: "json",
        success: function(data) {
            $("#restaurants-list").empty()
            var restaurants = data.restaurants
            for(var i=0; i<restaurants.length; i++) {
                $("#restaurants-list").append(
                      "<tr><td>"
                    + "<input type='checkbox' id='check" + restaurants[i].id + "'/>"
                    + restaurants[i].name
                    + "</td></tr>"
                );
                restaurant_checkboxes.push(restaurants[i].id);
            }
        }
    });
})

function create() {
    let feedback = validate_input();
    if(feedback.error) {
        $("#feedback").html(
            '<div class="panel panel-danger">'
          + '<div class="panel-heading">Erreur</div>'
          + '<div class="panel-body">' + feedback.error + '</div>'
          + '</div>'
        );
    } else {
        $.ajax({
            url: "action_servlet",
            data: {
                "action": "create-news",
                "title": $("#title").val(),
                "content": $("#content").val(),
                "start": $("#start-date-picker").val(),
                "end": $("#end-date-picker").val(),
                "restaurants": get_selected_restaurants()
            },
            dataType: "json",
            success: function(data) {
                redirect("admin.html");
            }
        });
    }
}

function validate_input() {
    if(!$("#title").val()) {
        return {error: "La nouvelle doit avoir un titre"};
    }
    if(!$("#content").val()) {
        return {error: "La nouvelle doit avoir une description"};
    }
    if(!$("#start-date-picker").val()) {
        return {error: "La nouvelle doit avoir une date de début"};
    }
    if(!$("#end-date-picker").val()) {
        return {error: "La nouvelle doit avoir une date de fin"};
    }
    if(get_selected_restaurants().length == 0) {
        return {error: "La nouvelle doit concerner au moins un restaurant"};
    }
    return {success: "Formulaire complet"};
}

function get_selected_restaurants() {
    let restaurant_ids = [];
    restaurant_checkboxes.forEach(function(id) {
        if($("#check" + id).is(':checked')) {
            restaurant_ids.push(id);
        }
    });
    return restaurant_ids;
}
