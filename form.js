

$(document).ready(function(){
    $("")
    $("form").submit(function(event){
      var data = JSON.stringify($("form").serializeJSON());
      var xhttp = new XMLHttpRequest();
      xhttp.open('POST','http://35.196.237.62/postData', true);
      // xhttp.setRequestHeader("Content-Length", Object.keys(data).length);

      xhttp.send(data);
      console.log(data);
      // window.location.href = ("submitted.html");
    });
});
