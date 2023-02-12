$(document).ready(function() {
    var xy = [];
    $("#c_ontainer").mousemove(function(event) {
      xy.push({x: event.pageX, y: event.pageY});
      console.log(event.pageX, event.pageY);
    });

    $(window).unload(function() {
      $.ajax({
        type: "POST",
        url: "/save_data",
        data: {data: xy}
      });
    });
  });

  $(document).ready(function() {
    var updateGraph = function() {
      $.ajax({
        url: "/graph_data",
        type: "GET",
        success: function(response) {
          // Parse the response JSON into an array of data points
          var data = response;
  
          // Plot the data using a library such as D3.js or Highcharts (instead of python plot)
          // ...
        }
      });
    };
  
    // Update the graph every time the mouse moves
    $(document).mousemove(updateGraph);
    
  });


  $(document).mousemove(function(event) {
    var x = event.clientX;
    var y = event.clientY;
    $.ajax({
      url: "/update_data?x=" + x + "&y=" + y,
      type: "GET",
      success: function(response) {
        console.log(response);
      }
    });
  });