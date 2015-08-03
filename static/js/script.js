$(".slider").slider({});

$(".pagination .disabled a, .pagination .active a").click(function(event) {
    event.preventDefault();
});

function sendMail(email, property) {
    window.location.href = "mailto:"+email+"?&subject=I'm interested in your property "+property;
}
