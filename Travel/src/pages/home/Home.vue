<template>
    <div>
        <home-header></home-header>
        <home-swiper></home-swiper>
        <home-icons></home-icons>
        <home-recommend></home-recommend>
    </div>
</template>

<script>
import HomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeIcons from './components/Icons'
import HomeRecommend from './components/Recommend'
import axios from 'axiso'
export default {
    name: 'Home',
    components: {
        HomeHeader,
        HomeSwiper,
        HomeIcons,
        HomeRecommend
    },
    methods: {
        getHomeInfo () {
            axios.get('/api/test.json')
                .then(this.getHomeInfoSuss)
        },
        getHomeInfoSuss (res) {
            console.log(res)
        }
    },
    mounted () {
        this.getHomeInfo()
    }
}
</script>

