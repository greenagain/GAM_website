$(document).ready(function() {
    $('.counter').counterUp({
        delay: 10,
        time: 1000
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
})