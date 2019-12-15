function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);

		var xhr=new XMLHttpRequest();
		const baseUrl = "http://0.0.0.0:5000/localPrediction/"
        var data = JSON.stringify({'url': tablink})
		//xhr.responseType = 'json'
		xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $("#div1").text(this.responseText)
       }
    };
		xhr.open("POST",baseUrl,true);
		xhr.setRequestHeader("Content-type", "application/json");
		xhr.send(data);
	});
}




$(document).ready(function(){
    $("button").click(function(){	
		var val = transfer();
    });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});
