$(document).ready(function() {
    $("#test1").click(function(){
        var json = {
            "data": {
                "type": "bicycle",
                "serial_number": "abcd1234",
                "manufacturer": "bkfab"
            }, "keychain": {
                "private": "test",
                "public":  "test"
            }
        };

        $.post("create", json, null, "json");

        // $.ajax({
        //     url: 'create',
        //     type: 'POST',
        //     data: json,
        //     contentType: 'application/json; charset=utf-8',
        //     dataType: 'json',
        //     async: false,
        //     success: function(msg) {
        //         alert("test");
        //     }
        // })
    })
})
