<template>
    <div>
        <div class="search">
            <input class="search-input" v-model="keyword" type="text" placeholder="输入城市名或拼音">
        </div>
        <div class="search-content" ref="search" v-show="keyword">
          <ul>
            <li class="search-item border-bottom" 
            v-for="item of list" :key="item.id">
              {{item.name}}</li>
            <li class="search-item border-bottom" v-if="!list.length">没有找到符合条件的城市</li>
          </ul>
        </div>
    </div>
</template>

<script>
import Bscroll from 'better-scroll'
export default {
  name: 'CitySearch',
  props: {
    cities: Object
  },
  data () {
    return {
      keyword: '',
      list: [],
      timer: null
    }
  },
  watch: {
    keyword () {
      if (this.timer) {
        clearTimeout(this.timer)
      }
      if (!this.keyword) {
        list = []
        return
      }
      this.timer = setTimeout(() => {
        const result = []
        let ct = this.cities
        for (let i in this.cities) {
          for (let j in ct[i]) {
            if (ct[i][j].spell.indexOf(this.keyword) > -1 || ct[i][j].name.indexOf(this.keyword) > -1) {
              result.push(ct[i][j])
            }              
          }
        }
        this.list = result
      },100)
    }
  },
  mounted () {
    this.scroll = new Bscroll(this.$refs.search)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .search
    height: .72rem
    padding: 0 .1rem
    background: $bgColor
    .search-input
      box-sizing: border-box
      height: .62rem
      line-height: .62rem
      width: 100%
      text-align: center
      border-radius: .06rem
      color: #666
      padding: 0 .1rem
  .search-content
    z-index 1
    overflow hidden
    position absolute
    top 1.58rem
    right 0
    bottom 0
    left 0
    background #eee
    .search-item
      line-height .62rem
      padding-left .2rem
      color #666
    // z-index: 1
    // overflow: hidden
    // position: absolute
    // top: 1.58rem
    // left: 0
    // right: 0
    // bottom: 0
    // background: #eee
    // .search-item
    //   line-height: .62rem
    //   padding-left: .2rem
    //   background: #fff
    //   color: #666
</style>
