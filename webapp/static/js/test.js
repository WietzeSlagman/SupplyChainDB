$(document).ready(function() {
    $("#test1").click(function(){
        $.post(
            "create",
            {
                "data": {
                    'type': 'bicycle',
                    'serial_number': 'abcd1234',
                    'manufacturer': 'bkfab'
                },

                "keychain": {
                    "private": "test",
                    "public":  "test",
                }
            }
        )
    })
})
