
var currentState = 0; //0:nothing, 1: C popup, 2: C++ popup, etc. 

// Remember that these should be possible to simply insert into the middle of the page, just have a styled body part.
var CPage = `

`
var CppPage = `

`
var CsPage = `

`
var PyPage = `

`
var JavaPagev = `

`
var JsPage = `

`
$(function () {
  


  $("#CLogo").on("click", function(event){
    currentState = 1;
    $("#placehold").html("<p>Become C page!</p>");
    });
  
  $("#CppLogo").on("click", function(event){
    currentState = 2;
    $("#placehold").html("<p>Become C++ page!</p>");
  });
  $("#CSLogo").on("click", function(event){
    currentState = 3;
    $("#placehold").html("<p>Become C# page!</p>");
  });
  $("#PyLogo").on("click", function(event){
    currentState = 3;
    $("#placehold").html("<p>Become Python page!</p>");
  });
  $("#JavaLogo").on("click", function(event){
    currentState = 3;
    $("#placehold").html("<p>Become Java page!</p>");
  });
  $("#JSLogo").on("click", function(event){
    currentState = 3;
    $("#placehold").html("<p>Become JavaScript page!</p>");
  });

});