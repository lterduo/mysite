<template>
	<view>
		<image :src="$baseUrl + '/static/customer/' + c_id + '.jpg'"></image>
		<view>
			姓名：{{customer.name}}
		</view>
		<view>
			性别：{{customer.gender}}
		</view>
		<view>
			<button type="primary">点击接待</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				c_id: "",
				customer: {}
			};
		},
		onLoad(msg) {
			console.log('msg: ', msg)
			this.c_id = msg.id.substring(0, msg.id.length - 4)
			console.log('cid: ', this.c_id)

			// 获取客户信息
			let url = this.$baseUrl + '/api/customer/?c_id=' + this.c_id
			console.log(url)
			uni.request({
				url: url,
				success: (res) => {
					console.log(' res: ', res);
					if (res.statusCode === 200) {
						if (res.data.results[0]) {
							this.customer = res.data.results[0]
						}
					}
				}
			})
		},
		methods: {

		}
	}
</script>

<style lang="less">
</style>
