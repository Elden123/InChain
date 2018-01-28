

$(document).ready(function(){
    $("form").submit(function(event){
      var data = ($("form").serializeJSON());
      var xhttp = new XMLHttpRequest();
      xhttp.open('GET','/server', true);
      xhttp.send(data);
    });
});
