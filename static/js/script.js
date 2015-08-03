$(".slider").slider({});

$(".pagination .disabled a, .pagination .active a").click(function(event) {
    event.preventDefault();
});
$(function() {

	function search() {

	        $.ajax({
	            url : "search/", // the endpoint
	            type : "POST", // http method
	            data : { search : $('#search').val() }, // data sent with the post request
	            // handle a successful response
	            success : function(json) {
	                $('#search').val(''); // remove the value from the input

	                $("#talk").prepend("<li><strong>"+json.title+"</strong></li>");

	            },
	            // handle a non-successful response
	            error : function(xhr,errmsg,err) {
	                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
	                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom

	            }
	        });
	    };
	 $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
 });

function sendMail(email, property) {
    window.location.href = "mailto:"+email+"?&subject=I'm interested in your property "+property;
}
