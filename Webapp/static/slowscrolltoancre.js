function slowscrolltoancre() {
	
	// Cache selectors
	var topMenu = $(".myMenu");
	var topMenuHeight = $("#header_end").offset().top+50;
	
	// All list items
	var menuItems = topMenu.find("a");
	
	// Anchors corresponding to menu items
	var scrollItems = menuItems.map(function(){
		var item = $($(this).attr("href"));
		if (item.length) { return item; }
		});


	// Bind click handler to menu items
	menuItems.click(function(e){
		openmenu();
		var href = $(this).attr("href"),
		offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight;
		$('body, html').animate({
	 scrollTop: offsetTop
	     }, 800);
	     menuItems.removeClass("active");
			 $(this).addClass("active");
	     return false;
	});

	// Bind to scroll
	$(window).scroll(function(){
		// Get container scroll position
		var fromTop = $(this).scrollTop()+topMenuHeight;
		
		// Get id of current scroll item
		var cur = scrollItems.map(function(){
			if ($(this).offset().top < fromTop) {
				return $(this); 
			}
		});
		
		// Get the id of the current element
		cur = cur[cur.length-1];
		var id = cur && cur.length ? cur[0].id : "";
		var lastId;
		
		if (lastId !== id) {
			lastId = id;
			// Set/remove active class
			menuItems.removeClass("active");
			menuItems.filter("[href=#"+id+"]").addClass("active");
		}
	});
}