<template>
    <div>
        <city-header></city-header>
        <city-search :cities="cities"></city-search>
        <city-list 
            :cities="cities" 
            :hotCities="hotCities" 
            :letter="letter"
        >
        </city-list>
        <city-alphabet 
            :cities="cities"
            @change="handleLetterChange"
        >
        </city-alphabet>
    </div>
</template>

<script>
import axios from 'axios'
import CityHeader from './components/CityHeader'
import CitySearch from './components/Search'
import CityList from './components/List'
import CityAlphabet from './components/Alphabet'

axios.defaults.baseURL = 'http://localhost:8000'

export default {
    name: "City",
    components: {
        CityHeader,
        CitySearch,
        CityList,
        CityAlphabet
    },
    data () {
        return {
            cities: {},
            hotCities: [],
            letter:''
        }
    },
    methods: {
        getCityInfo () {
            axios.get('/vue_city')
                .then(this.getCityInfoSucc)
        },
        getCityInfoSucc (res) {
            res = res.data
            if(res.ret && res.data) {
                const data = res.data
                this.cities = data.cities
                this.hotCities = data.hotCities
                // console.log(this.cities)
            }
        },
        handleLetterChange (letter) {
            // console.log(letter)
            this.letter = letter
        }
    },
    mounted () {
        this.getCityInfo()
    }
}
</script>

<style lang="stylus" scoped>

</style>

