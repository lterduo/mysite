<template>
	<view>
		匹配到客户：
		{{customer}}
	</view>
</template>

<script>
	export default {
		data() {
			return {
				customer: {}
			}
		},
		onLoad() {
			// this.getCustomer()
			uni.$on('customerMatched',(cm)=>{
				this.customer = cm
				console.log(cm)
			})
		},
		onUnload() {
			// 移除监听事件  
			uni.$off('customerMatched');
		},
		methods: {
			getCustomer() {
				console.log('getCustomer')
				var url = 'http://39.99.231.153:8000/api/customerMatched/'
				uni.request({
					url: url,
					success: (res) => {
						console.log(res);
						this.customer = res.data.customer
					}
				});
			}
		}
	}
</script>

<style>

</style>
