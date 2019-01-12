<template>
  <swiper :options="swiperOption">
    <!-- slides -->
    <swiper-slide v-for="item of swiperList" :key=item.id>
        <img class="swiper-img" :src="item.imgUrl" />
    </swiper-slide>
    <!-- Optional controls -->
    <div class="swiper-pagination"  slot="pagination"></div>
    <!-- <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
    <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
  </swiper>
</template>

<script>
export default {
    name: 'HomeSwiper',
    data() {
        return {
            swiperOption: {
                pagination: '.swiper-pagination',
                loop: true
            },
            swiperList: [{
                    id: '0001', imgUrl: 'http://img1.qunarzz.com/piao/fusion/1712/56/5e42f6256834402.jpg_890x330_567b0569.jpg'
                },
                {
                    id: '0002', imgUrl: 'http://img1.qunarzz.com/piao/fusion/1712/d0/0f5f1844045c0102.jpg_890x330_68cb5860.jpg'
                }
            ]
        }
    }
}
</script>

<style lang="stylus" scoped>
    .swiper-img
        width 100%
</style>
