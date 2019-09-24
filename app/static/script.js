// $('.site-nav-link').click(function () {
//     $(this).parents('.site-nav-item').addClass('active').siblings().removeClass('active').css({
//         'background-color': 'yellow'
//     })
// })
$(".site-nav-link").click(e => {
  $(e.target)
    .append('<span class="sr-only">(current)</span>')
    .closest(".site-nav-item")
    .addClass("active")
    .siblings(".site-nav-item")
    .removeClass("active")
    .find('.sr-only').remove();
});