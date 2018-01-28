$(document).ready(function(){
    $("form").submit(function(event){
      console.log($(this).serialize());
      event.preventDefault();
    });
});
