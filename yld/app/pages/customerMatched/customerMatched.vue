<template>
  <view>
    <view class="customer-list">
      <!-- <view class="customer-img" v-for="item in customerImg" :key="item.id">
        <image :src="item.url" mode="scaleToFill" @tap="customerInfo"></image>
      </view> -->
      <view class="customer-img" v-for="item in customer">
        <image :src="$baseUrl + '/static/customer/' + item" mode="scaleToFill" @click="customerInfo(item)"></image>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data () {
    return {
      userid: '',
      // customer为测试数据
      customer: ["2021-01-02_15_55_58.310257.jpg",
        "2021-01-02_15_55_58.314163.jpg",
        "2021-01-02_15_55_58.320752.jpg"
      ],
    }
  },
  onLoad () {
    //取得推送透传的信息
    uni.$on('customerMatched', (cm) => {
      this.customer = cm
      console.log(cm)
    })
    //获取userid
    try {
      this.userid = uni.getStorageSync('userid')
    } catch (error) {

    }
  },
  onUnload () {
    // 移除监听事件  
    uni.$off('customerMatched');
  },

  computed: {
    //   生成图片url
    customerImg () {
      let list = []
      for (let i = 0; i < this.customer.length; i++) {
        list[i] = {
          id: i,
          url: this.$baseUrl + '/static/customer/' + this.customer[i]
        }
      }
      return list
    }
  },
  methods: {
    customerInfo (item) {
      console.log('item: ', item)
      let url = '/pages/customerInfo/customerInfo?id=' + item
      uni.navigateTo({
        url: url
      })
    }
  }
}
</script>

<style lang="less">
.customer-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: flex-start;
  padding-left: 20rpx;
  .customer-img {
    width: 33%;
    height: 250rpx;
    image {
      width: 90%;
      height: 240rpx;
    }
  }
}
</style>
