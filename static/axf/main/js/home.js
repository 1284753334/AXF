$(function () {
 InitTopSwiper();
 InitTSwiperMenu();


})

function InitTopSwiper() {
     var swiper= new Swiper('#topSwiper',{
        loop:true,
        autoplay:3000,
        pagination: '.swiper-pagination'

    });

}

 function InitTSwiperMenu() {
     var swiper = new Swiper('#SwiperMenu', {
        slidesPerView :'3'

     });
 }