var photoValidate = function() {
    var photo = $(this)["photo"];
    var email = $(this)["email"];
    if(photo == "") { alert("Please upload an image"); }
    if(email == "") { alert("Please enter an email"); }
}

$(document).ready(function () {
    // Delete photo....
    $(".del").on('click', function(e) {
        let id = $(this).attr('id');
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/DeletePhoto/" + id.substring(3, id.length + 1),
            success: function(result) {
                location.href = "/Postcards";
            },
            error: function(result) {
                location.href = "/Postcards";
            }
        });
    });
   
    // Create postcard from photo....
    $(".cr").on('click', function (e) {
        let id = $(this).attr('id');
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/CreatePostcard/" + id.substring(2, id.length + 1),
            success: function(result) {
                location.href = "/Postcards";
            },
            error: function(result) {
                location.href = "/Postcards";
            }
        });
    });

    // Send postcard to user....
    $(".snd").on('click', function (e) {
        let id = $(this).attr('id');
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/SendPostcard/" + id.substring(3, id.length + 1),
            success: function(result) {
                location.href = "/Postcards";
            },
            error: function(result) {
                location.href = "/Postcards";
            }
        });
    });
});