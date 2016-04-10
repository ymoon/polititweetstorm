$(document).ready(function(){
	$('.scrollspy').scrollSpy();

	//Check to see if the window is top if not then display button
	$(window).scroll(function(){
		if ($(this).scrollTop() > 100) {
			$('.scrollToTop').fadeIn();
		} else {
			$('.scrollToTop').fadeOut();
		}
	});
	
	//Click event to scroll to top
	$('.scrollToTop').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});
});

snowStorm.snowColor = '#99ccff'; // blue-ish snow!?
snowStorm.flakesMaxActive = 96;  // show more snow on screen at once
snowStorm.useTwinkleEffect = true; // let the snow flicker in and out of view
snowStorm.followMouse = false;


function initialize() {
	var mapProp = {
		center:new google.maps.LatLng(51.508742,-0.120850),
		zoom:5,
		mapTypeId:google.maps.MapTypeId.ROADMAP
	};
	var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
}
google.maps.event.addDomListener(window, 'load', initialize);