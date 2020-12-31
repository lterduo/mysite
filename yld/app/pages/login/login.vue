<template>
  <view>
    <button @click="login">登录</button>
  </view>
</template>

<script>
export default {
  data () {
    return {

    };
  },
  methods: {
    login () {
      uni.switchTab({
        url: '/pages/index/index'
      })
    }
  }
}
</script>

<style lang="less">
</style>
