// $('.nav__toggle-btn').click(function () {
//     $(this).toggleClass('active');
//     console.log("Clicked menu button");
//     $("#mainListDiv").toggleClass("nav__wrapper--visible");
//     $("#mainListDiv").fadeIn();
//
// });

$(window).scroll(function() {
    if ($(document).scrollTop() > 200) {
        $('.navbar').addClass('highlight');
    } else {
        $('.navbar').removeClass('highlight');
    }
});
