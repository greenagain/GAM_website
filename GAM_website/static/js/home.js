(function ($) { $(document).ready(function() {
    // $('.counter').counterUp({
    //     delay: 10,
    //     time: 1000
    // });
    function comma(num) {
        var parts = num.toString().split(".");
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        return parts.join(".");
    };
    $('.count').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

    $('.home-link').hover(
        function() {
            $(this).find('p').css({
                'background-color': '#5E8F3A',
                'padding-right': '15%',
            })
        }, function() {
            $(this).find('p').css({
                'background-color': '#26361B',
                'padding-right': '10%',
            })
        }
    )
});
})(jQuery);
