<script>
	export default {
		data(){
			return{
				clientid:''
			}
		},
		onLaunch: function() {
			this.pushListener()
			
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		},
		
		methods:{
			pushListener() {
				
				this.clientid = plus.push.getClientInfo().clientid
				if (!this.clientid) { //如果获取的cid为空，说明客户端向推送服务器注册还未完成，可以使用setTimeout延时重试。
					setTimeout(() => {
						this.clientid = plus.push.getClientInfo().clientid
					}, 3000)
					console.log(this.clientid)
				}
				console.log(this.clientid)
				// 点击通知消息
				plus.push.addEventListener('click', (message) => {					
					console.log(message)					
					// 跳转到客户匹配页面
					uni.switchTab({
					  url: '/pages/customerMatched/customerMatched'
					})
					// 如果页面没有打开，将不能 注册监听事件
					uni.$emit('customerMatched',message) 
				});
				// 透传消息
				plus.push.addEventListener('receive', (message) => {			        
					console.log(message)
					uni.$emit('customerMatched',message)
				});
			},
			 
			pushCallBack() {
				
			}
		}
	}
</script>

<style>
	/*每个页面公共css */
</style>
