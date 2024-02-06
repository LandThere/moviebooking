const movieContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

movieContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
    

})



const swiper = new Swiper('.swiper', {
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
loop: true,

pagination: {
    el: '.swiper-pagination',
    clickable: true,
},

navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
},

});

AOS.init();