<template>
    <div>
        <city-header></city-header>
        <city-serch></city-serch>
        <city-list :cities="cities" :hotCities="hotCities"></city-list>
        <city-alphabet :cities="cities"></city-alphabet>
    </div>
</template>

<script>
import axios from 'axios'
import CityHeader from './components/CityHeader'
import CitySerch from './components/Serch'
import CityList from './components/List'
import CityAlphabet from './components/Alphabet'

axios.defaults.baseURL = 'http://localhost:8000/vue_city'

export default {
    name: "City",
    components: {
        CityHeader,
        CitySerch,
        CityList,
        CityAlphabet
    },
    data () {
        return {
            cities: {},
            hotCities: []
        }
    },
    methods: {
        getCityInfo () {
            axios.get()
                .then(this.getCityInfoSucc)
        },
        getCityInfoSucc (res) {
            res = res.data
            if(res.ret && res.data) {
                const data = res.data
                this.cities = data.cities
                this.hotCities = data.hotCities
                console.log(this.cities)
            }
        }
    },
    mounted () {
        this.getCityInfo()
    }
}
</script>

<style lang="stylus" scoped>

</style>

