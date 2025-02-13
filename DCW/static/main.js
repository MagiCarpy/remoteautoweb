// Detect when device switch is flipped
$(document).ready(function() {
    $("#switch").change(function() {
        var switchName = $(this).attr("name");
        var switchState = $(this).is(":checked") ? 1 : 0;
        console.log("Switch state:", switchState);
        $.ajax({
            url: "/devices",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                "deviceName": switchName,
                "status": switchState,

            }),
            success: function(response) {
                console.log("Success: ", response);
            },
            error: function(error) {
                console.error("Error", error);
            }
        });
    });
});
