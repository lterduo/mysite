<template>
    <div class="icons">
        <swiper :options="swiperOption" v-if="showSwiper">
            <swiper-slide v-for="(page,index) of pages" :key="index">
                <div class="icon"  v-for="item of page" :key=item.id>
                    <div class="icon-img">
                        <img class="icon-img-content" :src="item.imgUrl" />
                    </div>
                    <p class="icon-desc">{{item.desc}}</p>
                </div>
            </swiper-slide>
        </swiper>
    </div>
</template>

<script>
export default {
    name: 'HomeIcons',
    props: {
        iconList: Array
    },
    data() {
        return {
            swiperOption: {
                loop: true
            }
        }
    },
    computed: {
        pages () {
            const pages = []
            this.iconList.forEach((item,index) =>{
                const page = Math.floor(index/8)
                if (!pages[page]) {
                    pages[page] = []
                }
                pages[page].push(item)
            })
            return pages
        },
        showSwiper () {
            return this.iconList.length
        }
    }
}
</script>

<style lang="stylus" scoped>
    @import '~@/assets/styles/mixins.styl'
    .icons >>> .swiper-container
        height 0
        padding-bottom 50%
        .icon
            position relative
            overflow hidden
            float left
            height 0
            width 25%
            padding-bottom 25%
            .icon-img
                box-sizing border-box
                padding 5px
                position absolute
                top 0
                left 0
                right 0
                bottom 11px
                .icon-img-content
                    display block
                    margin 0 auto
                    height 100%
            .icon-desc
                position absolute
                left 0
                right 0
                bottom 0
                height 22px
                line-height 22px
                text-align center
                color #ccc
                //文字过长，后面用省略号，定义在
                ellipsis()
</style>
