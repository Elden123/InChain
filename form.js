

$(document).ready(function(){
    $("form").submit(function(event){
      var data = ($("form").serializeJSON());
      var xhttp = new XMLHttpRequest();
      xhttp.open('POST','http://35.196.237.62/postData', true);
      xhttp.send(data);
      console.log(data);
      // window.location.href = ("submitted.html");
    });
});
