function logout() {
    $.ajax({
        url: "/action_servlet",
        data: {
            "action": "logout"
        }
    });
    redirect("index.html");
}
