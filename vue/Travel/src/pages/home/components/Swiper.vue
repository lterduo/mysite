<template>
  <swiper :options="swiperOption" v-if="showSwiper">
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
    props: {
        swiperList: Array
    },
    data() {
        return {
            swiperOption: {
                pagination: '.swiper-pagination',
                loop: true
            }
        }
    },
    computed: {
        showSwiper () {
            return this.swiperList.length
        }
    }
}
</script>

<style lang="stylus" scoped>
    .swiper-img
        width 100%
</style>
