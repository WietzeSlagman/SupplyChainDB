$(document).ready(function() {
    $("#test1").click(function(){
        var json = {
            "data": {
                "type": "bicycle",
                "serial_number": "abcd1234",
                "manufacturer": "bkfab"
            }, "keypair": {
                "private": null,
                "public":  null
            }
        };

        send_json(json, "create", function() {
            alert("It worked!");
        })
    })

    $("#test2").click(function(){
        var json = {
            "data": {
                "token_for": {
                    "type": "bicycle",
                    "serial_number": "abcd1234",
                    "manufacturer": "bkfab"
                }
            },
            "keypair": {
                "private": null,
                "public":  null
            },
            "token_amount": 20
        };

        send_json(json, "create", function() {
            alert("It worked!");
        })
    })
})
