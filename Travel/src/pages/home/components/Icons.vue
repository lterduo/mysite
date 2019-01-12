<template>
    <div class="icons">
        <swiper >
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
export default{
    name: 'HomeIcons',
    data() {
        return {
            iconList: [{
                id: '0001',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '热门景点快点来玩啊大爷'
            },{
                id: '0002',
                imgUrl: 'https://fuss10.elemecdn.com/7/0a/af108e256ebc9f02db599592ae655jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '滑雪季'
            },{
                id: '0003',
                imgUrl: 'https://fuss10.elemecdn.com/c/7e/76a23eb90dada42528bc41499d6f8jpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '好吃的'
            },{
                id: '0004',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '好玩的'
            },{
                id: '0005',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '热门景点'
            },{
                id: '0006',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '热门景点'
            },{
                id: '0007',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '热门景点'
            },{
                id: '0008',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '热门景点'
            },{
                id: '0009',
                imgUrl: 'https://fuss10.elemecdn.com/3/01/c888acb2c8ba9e0c813f36ec9e90ajpeg.jpeg?imageMogr/format/webp/thumbnail/!90x90r/gravity/Center/crop/90x90/',
                desc: '来吧'
            },]
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
