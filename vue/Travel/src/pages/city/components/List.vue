<template>
  <div class="list" ref="wrapper">
    <div>
      <div class="area">
        <div class="title border-topbottom">当前城市</div>
        <div class="button-list" >
          <div class="button-wrapper">
            <div class="button">{{this.currentCity}}</div>
          </div>
        </div>
      </div>
      <div class="area">
        <div class="title border-topbottom">热门城市</div>
        <div class="button-list">
          <div class="button-wrapper" v-for="item of hotCities" :key="item.id" @click="handleCityClick(item.name)">
            <div class="button">{{item.name}}</div>
          </div>
        </div>
      </div>
      <div 
        class="area" 
        v-for="(item, key) of cities" :key="key"
        :ref="key"
      >
        <div class="title border-topbottom">{{key}}</div>
          <div class="item-list" v-for="innerItem of item" :key="innerItem.id" 
          @click="handleCityClick(innerItem.name)">
            <div class="item border-bottom">{{innerItem.name}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import BScroll from 'better-scroll'
export default {
  name: 'CityList',
  props: {
    cities: Object,
    hotCities: Array,
    letter: String
  },
  computed: {
    ...mapState({
      currentCity: 'city'
    })
  },
  methods: {
      handleCityClick (city) {
      // this.$store.dispatch('changeCity',city)
      this.changeCity(city)  //mapMutations映射后
      // this.$store.commit('changeCityMutation',city)
      this.$router.push('/')
    },
    //...mapMutations(['changeCityMutation'])
    ...mapMutations({
      changeCity: 'changeCityMutation'})
  },
  watch: {
    letter () {
      // console.log(this.letter)
      if (this.letter) {
        const element = this.$refs[this.letter][0]
        // console.log(element)
        this.scroll.scrollToElement(element)
      }
    }
  },
  mounted () {
    this.scroll = new BScroll(this.$refs.wrapper)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .border-topbottom
    &:before
      border-color #777
    &:after
      border-color #777
  .list
    overflow hidden
    position absolute
    top 1.58rem
    right 0rem
    bottom 0rem
    left 0rem
    .title
      line-height .54rem
      background #eee
      padding-left .2rem
      font-size .26rem
      color #666
    .button-list
      overflow hidden
      padding .1rem .6rem .1rem .1rem
      .button-wrapper
        float left
        width 33%
        .button
          margin .1rem
          text-align center
          border .02rem solid #ccc
    .item-list
      .item
        line-height .54rem
        color #666
        padding-left .2rem
</style>