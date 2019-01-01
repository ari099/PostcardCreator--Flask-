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
      }
   });
});