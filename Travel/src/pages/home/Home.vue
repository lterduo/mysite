<template>
    <div>
        <home-header ></home-header>
        <home-swiper :swiperList="swiperList"></home-swiper>
        <home-icons :iconList="iconList"></home-icons>
        <home-recommend></home-recommend>
    </div>
</template>

<script>
import HomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeIcons from './components/Icons'
import HomeRecommend from './components/Recommend'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'  

export default {
    name: 'Home',
    components: {
        HomeHeader,
        HomeSwiper,
        HomeIcons,
        HomeRecommend
    },
    data () {
        return {
            swiperList: [],
            iconList: []
        }
    },
    methods: {
        getHomeInfo () {
            axios.get('/vue_home')
                .then(this.getHomeInfoSuss)
        },
        getHomeInfoSuss (res) {
            res = res.data
            const data = res.data
            this.swiperList = data.swiperList
            this.iconList = data.iconList
        }
    },
    mounted () {
        this.getHomeInfo()
    }
}
</script>

