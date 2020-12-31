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
				
				plus.push.addEventListener('click', (message) => {
					this.pushCallBack()
					console.log(message)
				});
			 
				plus.push.addEventListener('receive', (message) => {
			        this.pushCallBack()
					console.log(message)
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
