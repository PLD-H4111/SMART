function redirect(url) {
    window.location.href = url;
}

function create_status(status) {
    if(status == "open" || status == 1) {
        return "<span class='status_open'>OUVERT</span>";
    }
    if(status == "closed" || status == 0) {
        return "<span class='status_closed'>FERME</span>";
    }
}

function create_eta(eta) {
    if(eta == "N/A") {
        return eta;
    }
    return eta + " min";
}

