$(document).ready(function(){
    // $(window).bind('scroll', function() {
    //     var navHeight = 300; // custom nav height
    //     ($(window).scrollTop() > navHeight) ? $('nav').addClass('goToTop') : $('nav').removeClass('goToTop');
    // });

    // $(window).scroll(function () {
    //     //if you hard code, then use console
    //     //.log to determine when you want the
    //     //nav bar to stick.
    //     console.log($(window).scrollTop());
    //     if ($(window).scrollTop() > 46) {
    //         $('.navbar').addClass('navbar-fixed-top');
    //     }
    //     if ($(window).scrollTop() < 47) {
    //         $('.navbar').removeClass('navbar-fixed-top');
    //     }
    // });
    // var MQL = 1170;

    //primary navigation slide-in effect
    // if($(window).width() > MQL) {
    //     var headerHeight = $('.navbar').height();
    //     $(window).on('scroll',
    //         {
    //             previousTop: 0
    //         },
    //         function () {
    //             var currentTop = $(window).scrollTop();
    //             //check if user is scrolling up
    //             if (currentTop < this.previousTop ) {
    //                 //if scrolling up...
    //                 if (currentTop > 0 && $('.navbar').hasClass('is-fixed')) {
    //                     $('.cd-header').addClass('is-visible');
    //                 } else {
    //                     $('.cd-header').removeClass('is-visible is-fixed');
    //                 }
    //             } else {
    //                 //if scrolling down...
    //                 $('.cd-header').removeClass('is-visible');
    //                 if( currentTop > headerHeight && !$('.cd-header').hasClass('is-fixed')) $('.cd-header').addClass('is-fixed');
    //             }
    //             this.previousTop = currentTop;
    //         });
    // }




    $(window).bind('scroll', function () {
        if ($(window).scrollTop() > 100) {
            $('.navbar').removeClass('m-t-46');
        } else {
            $('.navbar').addClass('navbar-fixed-top');
        }
    });

    // $('nav').on('affix.bs.affix', function () {
    //     var navHeight = $('.navbar').outerHeight(true);
    //     $('#nav + .container').css('margin-top', navHeight);
    // });
    //
    // $('nav').on('affix-top.bs.affix', function () {
    //     $('#nav + .container').css('margin-top', 0);
    // });
});

