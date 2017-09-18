function send_json(json, location, on_done) {
    // construct an HTTP request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", location, true);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

    // send the collected data as JSON
    xhr.send(JSON.stringify(json));

    xhr.onloadend = function () {
        // done
        on_done()
    };
}