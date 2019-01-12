<template>
    <div class="header">
        <div class="header-left">
            <div class="iconfont back-icon">&#xe624;</div>
        </div>
        <div class="header-input">
            <span class="iconfont">&#xe632;</span>
            输入城市/景点/主题
        </div>
        <div class="header-right">
            城市
            <span class="iconfont">&#xe62d;</span>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeHeader'
}
</script>

<style lang="stylus" scoped>
    @import '~@/assets/styles/varibles.styl'
    .header
        display flex
        line-height  43px
        background $bgColor
        color #fff
        .header-left
            width 32px
            float left
        .back-icon
            font-size 20px
            text-align center
        .header-input
            flex 1
            margin-top 6px
            margin-left 1px
            padding-left 10px
            height 32px
            line-height 32px
            background-color #fff
            border-radius 5px
            color #ccc
        .header-right
            width 62px
            float right
            text-align center
        
</style>

