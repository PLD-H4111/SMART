function notify(text) {
    if(window.Notification && Notification.permission === "granted") {
        var n = new Notification(text);
    }
    else if (window.Notification && Notification.permission !== "denied") {
        Notification.requestPermission(function(status) {
            if(Notification.permission !== status) {
                Notification.permission = status;
            }
            if(status === "granted") {
                var n = new Notification(text);
            }
        });
    }
}        

