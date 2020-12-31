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
				customer:[]
			}
		},
		onLoad() {
			this.getCustomer()
		},
		methods: {
			getCustomer(){
				console.log('getCustomer')
				var url = 'http://192.168.1.101:8000/api/customerMatched/'
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
