$(document).ready(function() {
   // Delete photo
   $("#del1").click(function(e) {
      e.preventDefault();
      $.ajax({
         type: "DELETE",
         url: "/DeletePhoto/1",
         success: function(result) {
            location.href = "/Postcards";
         },
         error: function(result) {
            location.href = "/Postcards";
            // alert(result);
         }
      });
   });
   
   // Create postcard from photo
   $("#cr1").click(function(e) {
      e.preventDefault();
      $.ajax({
         type: "POST",
         url: "/CreatePostcard/1",
         success: function(result) {
            location.href = "/Postcards";
         },
         error: function(result) {
            location.href = "/Postcards";
            // alert(result);
         }
      });
   });
});