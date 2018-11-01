$(function () {
    // 隐藏滚动条后，导致页面过大的一个处理
    $('.home').width(innerWidth)

    new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        //此参数设置为true时，点击分页器的指示点分页器会控制Swiper切换。
        paginationClickable: true,
        spaceBetween: 5,
        //默认第一块居左，设置为true后居中
        centeredSlides: true,
        autoplay: 2500,
        //用户操作swiper之后，是否禁止autoplay。默认为true：停止。
        autoplayDisableOnInteraction: false,
        loop: true
    });


     new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 10,
         loop: true
    });
})