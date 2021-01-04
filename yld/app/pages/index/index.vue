<template>
  <view class="container">
    <button class="submit" type="primary" @tap="logout">退出登录</button>
  </view>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  methods: {
    logout () {
      console.log('logout')
      try {
        uni.removeStorageSync('token')
        uni.navigateTo({
          url: '/pages/login/login',
        });

      } catch (error) {

      }
    }
  }
}
</script>

<style>
.container {
  padding: 20px;
  font-size: 14px;
  line-height: 24px;
}
</style>
