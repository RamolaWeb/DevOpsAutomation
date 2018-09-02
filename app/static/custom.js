jQuery(document).ready(function () {
	jQuery("#addUser").on("click", function(){
		var email = jQuery('input[name=email]').val();
		console.log(email);
		jQuery.ajax({
			type:"post",
			url:"/add/user",
			data:"email="+email,
			success:function(response){
				console.log(response)
				result = JSON.parse(response);
				console.log(result)
				console.log(result[message]);
			},
			failure:function(response){

			}
		});
	});

	jQuery(".deleteUser").on("click", function(){
		var id = jQuery(this).attr("id");
		jQuery.ajax({
			type:"post",
			url:"/delete/user",
			data:"id="+id,
			success:function(response){
				console.log(response)
			},
			failure:function(response){

			}
		});
	});
});
