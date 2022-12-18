
$(document).ready(function(){

  $("#day1_is").click(function(){
    $("#id_d1t1").empty();
    
    var dayOne_selection = $('#day1_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d1t1 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d1t1").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });


  $("#day1_is").click(function(){
    $("#id_d1t2").empty();
    
    var dayOne_selection = $('#day1_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d1t2 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d1t2").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day1_is").click(function(){
    $("#id_d1t3").empty();
    
    var dayOne_selection = $('#day1_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d1t3 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d1t3").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day2_is").click(function(){
    $("#id_d2t1").empty();
    
    var dayOne_selection = $('#day2_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d2t1 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d2t1").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day2_is").click(function(){
    $("#id_d2t2").empty();
    
    var dayOne_selection = $('#day2_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d2t2 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d2t2").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day2_is").click(function(){
    $("#id_d2t3").empty();
    
    var dayOne_selection = $('#day2_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d2t3 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d2t3").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });


  $("#day3_is").click(function(){
    $("#id_d3t1").empty();
    
    var dayOne_selection = $('#day3_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d3t1 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d3t1").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day3_is").click(function(){
    $("#id_d3t2").empty();
    
    var dayOne_selection = $('#day3_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d3t2 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d3t2").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day3_is").click(function(){
    $("#id_d3t3").empty();
    
    var dayOne_selection = $('#day3_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d3t3 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d3t3").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



  $("#day4_is").click(function(){
    $("#id_d4t1").empty();
    
    var dayOne_selection = $('#day4_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d4t1 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d4t1").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });


  $("#day4_is").click(function(){
    $("#id_d4t2").empty();
    
    var dayOne_selection = $('#day4_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d4t2 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d4t2").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });


  $("#day4_is").click(function(){
    $("#id_d4t3").empty();
    
    var dayOne_selection = $('#day4_is').find(":selected").text();
    $.ajax({
      url : "/done",
      type: "GET",
      data: {
        dayOne_selection: dayOne_selection
      },
      
      success: function(response){
        var length = $('#id_d4t3 > option').length;
        for(item of response.times){
          console.log(item);
          if(length === 0){
          $("#id_d4t3").append($('<option>',{value: item, text: item,}))
          }
        }
      }
    });
  });



});



  document.getElementById("fourth-desire").style.display = "none";
  // document.getElementById("fifth-desire").style.display = "none";
  // document.getElementById("desire-4").style.display = "none";

  


var check_value = document.getElementById("check-course")

check_value.addEventListener("change",function(e){
  if(check_value.checked){
    document.getElementById("fourth-desire").style.display = "initial";
    // document.getElementById("fifth-desire").style.display = "initial";
    // document.getElementById("desire-4").style.display = "initial";
  }else{
  document.getElementById("fourth-desire").style.display = "none";
  // document.getElementById("fifth-desire").style.display = "none";
  // document.getElementById("desire-4").style.display = "none";
  }
})


