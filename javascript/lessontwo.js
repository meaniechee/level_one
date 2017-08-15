// execute after document is loaded
$(document).ready(function(){
	// alert("you are NOT prepared");

	$("#id1").click(function(){
		$("#id1").hide(); // hide on click
	});


	$("#id2").click(function(){
		$("#id1").show(); // show id1 on click
	});

	$("#id3").click(function(){
		var id3 = $("#id3").text();
		$("#id3").text("NOT NOT"); // changing id3 text
	});

	$("#id7").click(function(){
		var id7 = $("#id6").val();
		alert(id7);
	});


	$("#id8").click(function(){
		var id8 = $("#id8").val();

		//ajax call
		$.ajax({
			url			: "myajax.php", // destination of script call
			type		: "POST", // sends a POST
			data		: id8,
			dataType	: "json", // receive data type in json format
			success		: function(data)
			{
				//Decode the data response
				// var test = decoded data
				// if test[0]['status'] == success
				// alert yay
				.done(function( msg ){
                msg = JSON.parse(msg);
			},
			error 		: function(xhr,textStatus,errorThrown)
			{

			}

		});
	});


}); // ending 

