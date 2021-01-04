## 页面通信

https://uniapp.dcloud.io/collocation/frame/communication

* uni.$emit(eventName,OBJECT)

  ~~~
  uni.$emit('login', {  
                  avatarUrl: 'https://img-cdn-qiniu.dcloud.net.cn/uploads/nav_menu/10.jpg',  
                  token: 'user123456',  
                  userName: 'unier',  
                  login: true  
              });
  ~~~

  

* uni.$on(eventName,callback)

  如果页面没有打开，将不能 注册监听事件

  ~~~
  onLoad(){  
      // 监听事件  
      uni.$on('login',(usnerinfo)=>{  
          this.usnerinfo = usnerinfo;  
      })  
  },  
  onUnload() {  
      // 移除监听事件  
          uni.$off('login');  
      },
  ~~~

  

## 页面导航

* https://uniapp.dcloud.io/api/router?id=navigateto

* 跳转到 tabBar 页面，只能用 uni.switchTab

  

## p31 

uni.request



# unipush

https://www.bilibili.com/video/BV1kE411J7Bo?p=7

https://blog.csdn.net/weixin_39288898/article/details/90769403?utm_source=app

* 编辑器中manifest.json--push--配置

* android应用签名

* 证书： https://ask.dcloud.net.cn/article/35777

* app代码 https://www.html5plus.org/doc/zh_cn/push.html

  * App.vue

    * onLaunch

    ~~~
    			// 点击通知消息时,执行该方法
    			plus.push.addEventListener("click",function(message){
    				// 自定义内容获取
    				let payload = message.payload
    				try{
    					//完成业务逻辑代码，如页面跳转，发送请求
    				}catch(e){
    					//TODO handle the exception
    				}
    			})
    			// 收到透传消息,执行该方法
    			plus.push.addEventListener("receive",function(message){
    				// 自定义内容获取
    				let payload = message.payload
    				try{
    					//完成业务逻辑代码
    				}catch(e){
    					//TODO handle the exception
    				}
    			})
    ~~~

* 服务端 https://docs.getui.com/

* 绑定cid

  ~~~
  // /App.vue
  onLaunch: function() {
  	// #ifdef APP-PLUS
  	const clientInfo = plus.push.getClientInfo()
  	console.log(clientInfo)
  	// #endif
  }
  ~~~

  

# 运行到手机 找不到手机

* 在任务管理器中找到adb.exe相关进程（包括kadb.exe等），干掉！

