
$(function(){
	
	
	$('#pais').on('change',function(){
		var id_pais =this.value;
		console.log(this.options[this.selectedIndex].text);	
		//-----	
		$.ajax({
			type: 'get',
			dataType: 'json',
			url: '/json/estados/'+id_pais,
			data: {},
		    success: function(data){			   
				//news = null;
				console.log(data);
				
			}
		});	
		//-------	
	
	});//end #pais

});

