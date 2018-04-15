// removes all empty paragraph tags (there are many produced by markdown translation)
$('p').filter(function () { return $.trim(this.innerHTML) == "" }).remove();

    var md;
    var scrollThrottle;
    var scrollFrozen = false;

    $(document).ready(function() {
        $("img").unveil(1000);
        md = new MobileDetect(window.navigator.userAgent);
        
        if (md.mobile() != null) { 
            $("#presentation-instructions").html('<img src="img/swipe-helper.gif" alt="swipe left or right for presentation mode.">');
            $("#presentation-instructions").css("background-color", "hsla(60, 100%, 50%, 0.5)");
            $("#presentation-instructions").css("left", "calc(50% - 30px)");
            $("#presentation-instructions").css("width", "60px");
            $("#presentation-instructions").css("height", "60px");
        } else { 
            $("#presentation-instructions").html("<- use the arrow keys ->");
        }
        
        //$("#test").velocity('transition.bounceUpIn', {delay: 250} ).velocity("reverse", { delay: 3000 });
        $("#presentation-instructions").velocity('transition.bounceDownIn', {delay: 500} ).velocity("transition.bounceUpOut", { delay: 3000 });        
        
        $(document).on('scroll', function() {

            if (md.mobile() == null && scrollFrozen == false) {
                var $videos = $("video");
                $.each($videos, function(index, video) {
                    var v = $(video).get(0);
                    if ( $(this).is( ':in-viewport' )) {
                        if (v.paused) {
                            //console.log('playing a paused video');
                            v.play();
                        } else {
                            //console.log('video is playing already');
                        }
                    } else {
                        if (!v.paused) {
                            //console.log('pausing video');
                            v.pause();
                        } else {
                            //console.log('video not in viewport');
                        }
                    }
                });

                scrollFrozen = true;
                scrollThrottle = setTimeout(function() { scrollFrozen = false; }, 25);

            } else {
                //alert('mobile');
            }

        });

    });

    var slide = 8;
    var slide_class = "slide";
    var press_is_on = false;
    var press_is_moving = false;
    var press_bounce;

    //var c_veil_opacity = 0.6;

    function enter_press_mode() {
      if(!press_is_on) {
        press_is_on = true;
        $(".veil").animate({opacity:0.95},250);
        $(".veil").css('opacity','0');
        $('.js--press-slack').addClass('press-slack');
        $(".presentation_control_wrapper").show();
      }
    }

    function exit_press_mode() {
      if(press_is_on) {
        press_is_on = false;
        $(".veil").animate({opacity:0},0);
        $('.js--press-slack').removeClass('press-slack');
        slide_reset(current_slide());
        scroll_center(current_slide(), 0);
        $(".presentation_control_wrapper").hide();
      }
    }

    function scroll_center(el, duration) {
      var offset = 0.5 * ($(window).height() - $(el).outerHeight());

      $.Velocity(el, 'scroll',{
        duration: duration,
        offset: -1 * offset,
        easing: 'ease-in-outs',
        queue: false
      });
    }

    function press_move(el) {

      enter_press_mode();
      slide_focus(el);

      press_is_moving = true;
      clearTimeout(press_bounce);
      press_bounce = setTimeout(function() {
        press_is_moving = false;
      }, 1500);

      $(el).css({"z-index": 200,});
      scroll_center(el, 1000);
      set_slide_label(slide);
    }

    function next() {
      // todo: check it's not at the end - would go to beginning
      if(slide < $("."+slide_class).length - 1) {
        var prev_slide = $("."+slide_class)[slide];
        slide_reset(prev_slide);
        if(press_is_on) {
          slide += 1;
        } else {
          slide = closest_slide();
        }
        var s = $("."+slide_class)[slide];
        press_move($(s));
      }
    }

    function prev() {
      if(slide > 0) {
        var prev_slide = $("."+slide_class)[slide];
        slide_reset(prev_slide);
        if(press_is_on) {
          slide += -1;
        } else {
          slide = closest_slide();
        }
        var s = $("."+slide_class)[slide];
        slide_reset(s);
        press_move($(s));
      }
    }

    function current_slide() {
      return $($("."+slide_class)[slide]);
    }

    function slide_reset(s) {
      $(s).css({"z-index":0});
      // $(s).removeClass('press-slack');
    }

    function slide_focus(s) {
      $(s).css({"z-index":200});
      // if($(s).hasClass('js--press-slack')) {
        // $(s).addClass('press-slack');
      // }
    }

    function set_slide_label(index) {
      var completion = (index + 1) / parseInt($(".slide").length);
      var slide_label = '<span class="opacity-half">' + (Math.round(completion*100)) + '%</span>';
      if(index == 0) slide_label = "Start";
      if(index == $(".slide").length-1) slide_label = "End";
      $(".presentation_control").html(slide_label);
    }

    function closest_slide() {
      if ($(window).scrollTop() < 150) return 0;
      var window_center_position = $(window).scrollTop() + $(window).height()*0.5;
      var slides = $(".slide");
      var min_distance = 99999;
      var closest_slide = 0;
      for (var i = 0; i < slides.length; i++) {
        var slide_center_position = $(slides[i]).offset().top + $(slides[i]).outerHeight() * 0.5;
        var distance = Math.abs(window_center_position - slide_center_position);
        if(distance < min_distance) {
            closest_slide = i;
            min_distance = distance;
        }
      }
      return closest_slide;
    }

    $(document).keydown(function(event) {
      if ( event.which == 37 || event.which == 38 ) {
        prev();
        event.preventDefault();
      } else if ( event.which == 39 || event.which == 40 ) {
        next();
        event.preventDefault();
      } else if ( event.which == 27 ) {
        exit_press_mode();
      }
    });

    $(document).scroll(function () {
      if(!press_is_moving) {
        exit_press_mode();
        set_slide_label(closest_slide());
      }
    });


var hammertime = new Hammer(document.body);
hammertime.on('swipeleft', function(ev) {
	//console.log(ev);
    //$(".debug-message").html("swipeleft");
    next();
});
hammertime.on('swiperight', function(ev) {
	//console.log(ev);
    //$(".debug-message").html("swiperight");
    prev();
});    
    