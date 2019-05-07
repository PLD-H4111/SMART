function redirect(url) {
    window.location.href = url;
}

function create_status(status) {
    if(status === "open") {
        return "<span class='status_open'>OUVERT</span>";
    }
    if(status === "closed") {
        return "<span class='status_closed'>FERME</span>";
    }
}

