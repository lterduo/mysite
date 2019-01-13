<template>
    <div>
        <city-header></city-header>
        <city-serch></city-serch>
        <city-list></city-list>
    </div>
</template>

<script>
import CityHeader from './components/CityHeader'
import CitySerch from './components/Serch'
import CityList from './components/List'
export default {
    name: "City",
    components: {
        CityHeader,
        CitySerch,
        CityList
    }
}
</script>

<style lang="stylus" scoped>

</style>

