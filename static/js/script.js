$(".slider").slider({});

$(".pagination .disabled a, .pagination .active a").click(function(event) {
    event.preventDefault();
})
$(function() {

	$('#search').keyup(function() {
	
	$.ajax({
		type: "POST",
		url: "/search/",
		data: {
			'search_text' : $('#search').val(),
			'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		},
		success: searchSuccess,
		dataType: 'html'
		});
	});
});

function searchSucess(data, textStatus, jqXHR)
{
	${'#search-results').html(data);
}