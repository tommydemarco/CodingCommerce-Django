document.addEventListener('DOMContentLoaded', function(){

    var fixmeTop = $('.header-wrap-stick').eq(0).offset().top;       // get initial position of the element
    var divHeight = $('.header-wrap-stick').eq(0).outerHeight();
    var headerHeight = $("#main-navigation").outerHeight();
    $(window).scroll(function() {                  // assign scroll event listener

        var currentScroll = $(window).scrollTop(); // get current position

        if (currentScroll >= fixmeTop) {           // apply position: fixed if you
            $('.header-wrap-stick').eq(0).css({
                top: 0,
            }).addClass('fixed-top')
            $('#content').css({
                paddingTop: divHeight
            })
        } else {                                   // apply position: static
            $('.header-wrap-stick').eq(0).css({
                top: 'auto'
            }).removeClass('fixed-top')
            $('#content').css({
                paddingTop: 0
            })
        }

        })
    })


  jQuery(window).on("load", function() {
     
    function handlePreloader() {
        var preloader = $('.preloader');
        if(preloader.length){
        preloader.delay(600).fadeOut(800);
        }
    }
    handlePreloader(); 
});