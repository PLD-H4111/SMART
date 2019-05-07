$(document).ready(function(){
    $('#input-password').keypress(function(e) {
        if(e.keyCode==13) {
            $('#submit-button').click();
        }
    });
    $('#input-login').keypress(function(e) {
        if(e.keyCode==13) {
            $('#submit-button').click();
        }
    });
});

function login() {
    let login = $("#input-login").val();
    let password = $("#input-password").val();
    
    if(!login || !password) {
        return;
    }
    
    $.ajax({
        url: "/action_servlet",
        type: "post",
        contentType: "application/json",
        data: JSON.stringify({
            "action": "admin-login",
            "login": login,
            "password": password
        }),
        dataType: "json",
        success: function(data) {
            if(data.success == 1) {
                window.location.href = "admin.html";
            } else {
                $("#feedback").html(
                    '<div class="card border-danger">'
                  + '<div class="card-header bg-danger text-white">Erreur</div>'
                  + '<div class="card-body">Identifiants de connexion invalides</div>'
                  + '</div>'
                );
            }
        }
    });
}

