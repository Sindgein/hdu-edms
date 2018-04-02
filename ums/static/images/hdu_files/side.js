var show = false;



$('.side-btn').on('click', function () {
    if (!show) {
        $('.side-back').fadeIn(400);
        $('.side-area').animate({right: 0}, 300);
        $('body').css('overflow-y', 'hidden');
    } else {
        $('.side-back').fadeOut(400);
        $('.side-area').animate({right: -225}, 300);
        $('body').css('overflow-y', 'visible');
    }
    show = !show;
});

$('.side-back').on('click', function () {
    show = false;
    $('.side-back').fadeOut(400);
    $('.side-area').animate({right: -225}, 300);
    $('body').css('overflow-y', 'visible');
});


(function () {
    var time = new Date();
    var y = time.getFullYear();
    var m = time.getMonth() + 1;
    var d = time.getDate();

    var x = time.getDay();

    var ar = ['日', '一', '二', '三', '四', '五', '六'];
    var str = '星期' + ar[x];

    $('.side-week').html(str);
    $('.side-data').html(y + '/' + m + '/' + d)

})()

$.ajax({
    url: '/index/getweather',
    dataType: 'json',
    success: function (data) {
        var t = data.weather[0]
        $('.ssw img').css('height', '40px');
        $('.ssw img').css('width', '40px');
        $('.ssw img').attr('src', '/asset/home/images/' + t.icon.slice(0, 2) + '.png')
        // $('.sst1').html(t.main)
        var max = (data.main.temp_max - 273.15).toFixed(0);
        var min = (data.main.temp_min - 273.15).toFixed(0);
        var map = {
            '01': '晴',
            '02': '晴多云',
            '03': '阴',
            '04': '阴多云',
            '09': '暴雨',
            '10': '雨',
            '11': '雷阵雨',
            '13': '雪',
            '50': '雾'
        }
        var text = map[t.icon.slice(0, 2)]
        text = text ? text : ''
        $('.sst1').html(text)
        $('.sst2').html(min + '~' + max + '℃')
        $('.sst3').html(data.wind.direction)
        $('.sst4').html(data.wind.level + '级')
        $('.side-weather').show()
    }

})

var ss;

$('.ff-show').hover(function(){
    clearTimeout(ss)
    
    var index = $(this).attr('data')
    $('.ff-manys').hide()
    $('.ai').removeClass()
    $(this).next().addClass('ai')
    $('.ff-manys').eq(index).show()

}, function(){

    ss = setTimeout(function(){
        $('.ff-manys').hide()
        $('.ai').removeClass()
    },300);
})

$('.ff-manys').hover(function(){
    clearTimeout(ss)
}, function(){
    
     ss = setTimeout(function(){
        $('.ff-manys').hide()
         $('.ai').removeClass()
    },300);
})






