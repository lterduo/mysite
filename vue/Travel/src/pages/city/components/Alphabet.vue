<template>
    <ul class="list" >
        <li class="item" 
            v-for="item of letters" 
            :key="item"
            @click="handleLetterClick"
            @touchstart="handleTouchStart"
            @touchmove="handleTouchMove"
            @touchend="handleTouchEnd"
            :ref="item"
        >
            {{item}}
        </li>
    </ul>
</template>

<script>
export default {
  name: 'CityAlphabet',
  props: {
      cities: Object
  },
  data () {
      return {
          touchStatus: false,
          startY: 0,
          timer: null //延时，优化性能
      }
  },
  updated () {
      this.startY = this.$refs['A'][0].offsetTop   //[0]才是dom元素。offsetTop是距离顶部的像素  264
  },
  computed: {
      letters () {
        //   console.log(this.cities)
          const letters = []
          for (let i in this.cities) {
              letters.push(i)
            //   console.log(i)
          }
        return letters
      }
  },
  methods: {
      handleLetterClick (e) {
        //   console.log(e.target.innerText)
          this.$emit('change',e.target.innerText)
      },
      handleTouchStart () {
          this.touchStatus = true
      },
      handleTouchMove (e) {
          if (this.touchStatus) {
              if (this.timer) {
                  clearTimeout(this.timer)
              }
              this.timer = setTimeout(() => {
                  //放入updated   const startY = this.$refs['A'][0].offsetTop   //[0]才是dom元素。offsetTop是距离顶部的像素  264
                const touchY = e.touches[0].clientY -74  //e是touch事件，e.touches[0]是手指信息，clientY是坐标  ,距离顶部，所以要减去74（header加input）
                const index = Math.floor((touchY - this.startY)/20)
                if (index >= 0 && index <= this.letters.length) {
                    this.$emit('change',this.letters[index])
                }
              }, 16)                
          }
      },
      handleTouchEnd () {
          this.touchStatus = false
      }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/varibles.styl'
  .list
    display flex
    flex-direction column
    justify-content center
    position absolute
    top 1.58rem
    right 0
    bottom 0
    // background-color red
    width .4rem
    .item
        line-height .4rem
        text-align center
        color $bgColor
</style>