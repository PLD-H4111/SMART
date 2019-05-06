function login() {
    let login = $("#input-login").val();
    let password = $("#input-password").val();
    
    $.ajax({
        url: "/action_servlet",
        data: {
            "action": "admin-login",
            "login": login,
            "password": password
        },
        dataType: "json",
        success: function(data) {
            if(data.success == 1) {
                window.location.href = "admin.html";
            } else {
                $("#feedback").html(
                    '<div class="panel panel-danger">'
                  + '<div class="panel-heading">Erreur</div>'
                  + '<div class="panel-body">Identifiants de connexion invalides</div>'
                  + '</div>"'
                );
            }
        }
    });
}
