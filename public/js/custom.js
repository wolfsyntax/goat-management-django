$(document).ready(function(){
	
	$('#example').DataTable();
	$('#damID-select').editableSelect();
	$('#sireID-select').editableSelect();
	
//	alert("Selected Category: " + $("[name='cflag']").val());
	
	if($("[name='cflag']").val() == 'True') {
		$(".pform").show();
		$(".biform").hide();
	}else if($("[name='cflag']").val() == 'False') {
		$(".pform").hide();
		$(".biform").show();	
	}else{
		$(".pform").hide();
		$(".biform").hide();
	}

	$('[name="body_color"]').tagify({
		delimiters: ",",
		pattern: null,
		maxTags: 3, //Infinity,
		addTagOnBlur: true,
		//allow duplicate tags
		//duplicates: false,
	});

/*
	$('input[name="date"]').daterangepicker();
	$('input[name="daterange"]').daterangepicker({

    	opens: 'left'
  	}, function(start, end, label) {
  		alert('test');
    	console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
  	});
*/

	tail.DateTime("#birth_date");
	tail.DateTime("#purchase_date");

	$("[name='category']").click(function(){ 
		if($(this).val() == 'purchase'){
			$(".pform").show();
			$(".biform").hide();
		} else if($(this).val() == 'birth'){
			$(".pform").hide();
			$(".biform").show();
		}
	});

});