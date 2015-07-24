// Property validator for the "addProperty.html" page

jQuery.validator.setDefaults({
    highlight: function(element) {
        jQuery(element).closest('.form-group').addClass('has-error');
    },
    unhighlight: function(element) {
        jQuery(element).closest('.form-group').removeClass('has-error');
    },
    errorElement: 'span',
    errorClass: 'label label-danger',
    errorPlacement: function(error, element) {
        if (element.parent('.input-group').length) {
        	// If there is a input-group to be found, then insert a danger label after the input-group
            error.insertAfter(element.parent());
        } else if (!element.siblings().filter('.label').length){
            error.insertAfter(element);
        }
    },
    invalidHandler: function(event, validator) {
    	console.log($('.label-danger'));
    	$('.label-danger').remove();
    }
});