$().ready(function(){
	// fixed header
	$header = $('#header');
	$(window).scroll(function() {
		// hideMenu();

	}); // window.scroll

	/************ nav menu sandwich **************/
	$sandwich = $('#sandwich');
	$body = $('body');
	$mask = $(document.createElement("div"))
	// hide menu when open and sandwich clicked
	function hideMenu() {
		$body.removeClass('smr-open');
			$mask.remove();
	}
	$sandwich.click(function(){
		if ($body.hasClass('smr-open')) {
			hideMenu();
		} else {
			$body.append($mask);
			$body.addClass('smr-open');
		}
	});
})