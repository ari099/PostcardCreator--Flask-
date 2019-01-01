$(document).ready({
   $("del1").ajax({
      url: '/DeletePhoto/',
      type: 'DELETE',
      success: function(result) {
         // Do something with the result
      }
   })
});