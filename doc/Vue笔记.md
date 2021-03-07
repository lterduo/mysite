



# 基础

## 指令
### [v-on](https://vuefe.cn/v2/guide/events.html)

- 作用:使用 `v-on` 指令绑定 DOM 事件，并在事件被触发时执行一些 JavaScript 代码。

- 语法:  @事件名.修饰符 = "methods中的方法名"  

- 注意: $event  可以传形参
- 修饰符

  - `.once` - 只触发一次回调。
  - `.prevent` - 调用 `event.preventDefault()`。

> 简写: @事件名.修饰符 = 'methods中的方法名'

### v-for
    v-for="(item,index) in list"
    v-for="(value,key,index) in object"
    加上key，渲染效率高
    v-for="(v,i) in list" :key="i"
    v-for="(v,k,i) in object" :key="i"


### v-bind
    v-bind:属性="值"
    常用简写    :
    <img :src="ooxx">
    
    绑定class时,用对象传值：
    <p :class="{left:a, active:b}"></p>
    data:{
        a:true,
        b:true
    }
    啰嗦，直接传数组。
    <input type="text" v-model="msg">
    <input :disabled="msg.length===0" type="button" value="add">
    只有输入框不为空时，add才可以点击

### 计算属性
    computed: {
                newList(){
                    if(this.searchVal == ''){
                        return this.list
                    }else{
                        return this.list.filter(item => item.includes(this.searchVal))
                    }
                },
            },
    啰嗦，不用判断直接return this.list.filter(item => item.includes(this.searchVal)) ，
    因为''包含在任何字符串中

### json-server     postman
### axios
    $ npm install axios
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="./axios.min.js"></script>

## 组件
建议: 在实际开发中,尽可能使用各种第三方组件
命名规范，p-h, 用减号报错概率最小
### 父子传值： 类似于变量的使用过程1、声明 2、赋值  3、使用
​    1、声明：c-c子组件中 props:['a']  
​    2、赋值：<c-c :a="msg"></c-c>   也就是绑定父组件的msg
​    3、使用：c-c的template中像data一样使用

## vue-router
    1、<router-link to="/a">A</router-link> 
        <router-link to="/b">B</router-link>
    2、<router-view></router-view>
    3、<script src="./vue-router.js"></script>
    4、var comA = { template: '<div>A</div>' }
       var comB = {template:'<div>B</div>'}
    5、var routes = [
            {path:'/a',component:comA},
            {path:'/b',component:comB}]
    6、var router =  new VueRouter({
            routes:routes
        })
    7、vue中注册
        el:'#app',
        router:router,
### 动态路由
    1、不同标识渲染同一组件 (to="/a",to="/b")都渲染comA
    2、{path: '/:d'} 点击哪个:d就变成哪个
    3、在视图中获得点击的id值  {{$route.params.id}}
### 重定向
    {path:'/', component: comA}
    {path:'/', redirect:{path:'/a'}}
    {path:'/', redirect:{name: 'aaa'}}
    一般用于首页重定向
    {path:'*', component: comA} 
    用户输错地址，重定向到指定页        建议写在最后
### 编程式导航
    <button @click="changeUrl()"
    methods:{
        changeUrl(){
            this.$router.push(path:'a')
        }
    }
### p85 tag
    在css中设置激活样式
    routerlink默认渲染是a标签，可以用tag="li"，修改成其他标签
### 二级路由

# cli 
全局安装
npm install -g @vue/cli
vue -V
如果仍然要使用vue-cli 2版本的指令 需要安装一个桥接工具
npm install -g @vue/cli-init

webpack-simple是一种工程模板
`vue init webpack-simple 项目名称`
cd 项目名称
npm i
npm run dev

安装其他工具，如bootstrap, 进入项目路径
cd C:\git\mysite\vue-manage\heroes53
npm i bootstrap@3.3.7       @跟版本号

### main.js
1、入口
2、导包，导入各种包
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
报错
./node_modules/bootstrap/dist/fonts/glyphicons-halflings-regular.ttf
ttf无法处理，需要修改webpack.config.js
{
    test: /.(ttf|woff2|woff|eot)$/,
        loader: 'file-loader',
            options: {
                name: '[name].[ext]?[hash]'
            }
}

# 快捷键	一键vue模板	
https://blog.csdn.net/qq_30763385/article/details/104802694
首选项》用户片段》vue，拷入代码段
新建vue，sca

# 使用组件
1、App.vue 
    import appNav from './components/common/appnav.vue'
    appNav 驼峰
2、compoments 中注册
    appNav:appNav       直接简写成  appNav
3、模板中使用
    <app-nav>   可以直接减号写法

1、引入 2、注册 3、使用

# 项目使用vue-router
 npm i vue-router

 1、设置 router-link
 2、App.vue 设置 router-view

 3、不要用main.js， 新建router/router.js, 导入vue和vue-router
    import Vue from 'vue'
    import VueRouter from 'vue-router'
    Vue.use(VueRouter) 
 4、导入要使用的组件
    import List from './components/list/list'
    ...
 5、配置路由
    var routes = [{name:'', path:'/list', component:List},]
 6、实例化
    var router = new VueRouter({
        routes
    })
 7、导出
    export default router

 8、main.js 使用
    import router from './router/router.js'
 9、mainn.js new Vue 中挂载
        el:'#app',
        router,
## linkExactActiveClass 全局设置激活 router-link 的类名
    linkExactActiveClass：'active'      active是一个存在的class名



# 模板methods使用数据
    1、如果有data，直接用
    2、如果没有data，考虑传参数。
       <a @click.prevent="deleteItem(item.id)">

# 两个组件跳转时传值    编程式导航和动态导航
    <a @click.prevent="showEditVue(item.id)">
    showEditVue(ID){
        this.$router.push(
            {name:'edit',
            params:{id:ID}
            })
    }
    router.js中添加路由
    {name:'edit',
    `path:'/edit/:id'`
    component:Edit}
    
    接收（被跳转到）的组件B，用this.$route.params.id接收，注意是$route, 不是$router
    this.$router    获取路由对象(router.js中的router)
    this.$route     获取路由配置对象，进一步获得信息（name,path,params...)

# 全局配置axios
axios请求在多个组件中都要使用, 所以, 可以考虑给Vue实例添加axios选项, 所有的组件都可以使用
`main.js` 
// 导入axios
import axios from 'axios';
// 配置所有Vue的实例都具有axios这个成员
Vue.prototype.axios = axios
任意地方都可以用this.axios来使用




# 后台管理项目
## 准备接口 django-rest-framework
## 脚手架安装
vue init webpack mallmanager53
## npm有时报错，清一下缓存
npm cache clean
报错就按照路径手动删除

## element ui
npm i element-ui -S
在main.js中
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
去官网找代码直接用



## css less 报错问题

https://blog.csdn.net/maidu_xbd/article/details/105779377



## 跨域问题
    django端解决
pip install django-cors-headers
INSTALLED_APPS = (
...
'corsheaders',   
...
)
MIDDLEWARE_CLASSES
= (
...   
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',   
...
)

CORS_ORIGIN_ALLOW_ALL = True  

## axios 用法

- npm i axios

- .then
  使用
      1、模板(list.vue) methods 
          getData(){
              axios.get().then(res=>{
                  this.list = res.data
              })
              }
      2、data(){return{data:[]}}
      3、mounted(){this.getData()}
      4、使用数据

- async await

  ```
  const res = await this.axios.post("api/users/", data);
  要在离await最近的函数前加上async
  ```

  ```
  deleteUser(){
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          }).then(async () => {
          
            const res = await this.axios.delete("api/users/");
            
          }).catch(() => {
          });
  ```

  注意：async是加载了箭头函数的前面

## axios 在项目中的应用（写成插件）
1. main.js 中
    import axios from 'axios'
    Vue.prototype.axios = axios
项目中可以直接用this.axios.get...
2. 不用1. 直接写成插件（麻烦，懒得写）
3. 优化 Url 在绑定原型前设置baseURL
    import axios from 'axios'
    `axios.defaults.baseURL = 'http://127.0.0.1:8000/'`
    Vue.prototype.axios = axios
模板中的url
    this.axios.post('api/book/',{name:'水浒传',price:88})

## token 登录
* 用localStorage.setItem('token',data.token)保存，其他页面要const token = localStorage.getItem("token")

登录成功时，保存正确用户token
localStorage.setItem('token',data.token)
home.vue中
    beforeCreate() {
    //获取token
    const token = localStorage.getItem("token");
    //如果没有，跳转登录
    if (!token) {
      this.$router.push({ name: "login" });
    }
    //如果有，继续渲染
  },
  methods:{
    logout(){
      //清除token
      localStorage.clear()
      this.$message.success('退出成功')
      this.$router.push({name:'login'})
    }
  }

## home布局
element中的container
头部 layout布局
## 侧边栏 导航 el-menu
    index不能相同
    :unique-opened="true"
    icon 图标
    :router="true"  相当于router-link
        index 相当于 path
        嵌套路由    home中的main里加<router-view>
        配置路由    home中设置children

## 用户列表
el-card 小容器 卡片 
<el-breadcrumb separator="/">
<el-input class="user-search" placeholder="请输入内容" v-model="query">
<el-table :data="users" style="width: 100%">
    <el-table-column type="index" prop="date" label="序号" width="180"></el-table-column>
绑定数据，类型为数组
element中找Table-column Attributes， type="index" 自增加

## token 授权
    137 需要授权的 API（除了login） ，必须在请求头中使用 Authorization 字段提供 token 令牌
    const AUTH_TOKEN = localStorage.getItem('token')
    this.axios.defaults.headers.common['Authorization'] = AUTH_TOKEN
### 服务器端

## 全局过滤器 处理时间格式 p145
在main.js中，new Vue 前
Vue.filter('fmtdate',(v)=>{
    return moment(v).format('YYYY-MM-DD')
})
注意，先 npm i moment ，再在 main.js中 import momnet
### 组件中使用组件，或者插值
    <el-table-column>
        <template>
            <el-switch>
        </template>
### slot-scope

组件中插入组件，用\<template>标签包裹，并写好绑定的数据\<template slot-scope="scope">

此时父标签绑定的数据可以删除，如下例中的prop="create_time" 可删除，因为子组件中已经取到了create_time

    在要显示的标签中：
        <el-table-column prop="create_time" label="创建时间" width="120">
            <template slot-scope="scope">
                {{scope.row.create_time | fmtdate}}
            </template>
        </el-table-column>
    用 slot-scope 属性指出数据源（名字随便起，会自动找到上层绑定的数据，也就是<el-table :data="users" ）， 用差值表达式使用数据 | 使用过滤器。此时prop="create_time"可以删除
## 字符串 拼接 变量
methods: {
  showMsg() {
    alert(`获取了${a}`);
  }
}
不是单引号，而是两个 ` 号

## axios post 返回 bad request

要检查是否字段错误。drf没有返回具体错误



## 动态导航	根据角色生成菜单

* p232
* p233

## 路由卫士

* p234



## 富文本编辑器 quill

* p250

* 安装：

  ```
  npm install vue-quill-editor --save
  ```

* 挂载

  * 全局

  * 局部

    ```
    import 'quill/dist/quill.core.css'
    import 'quill/dist/quill.snow.css'
    import 'quill/dist/quill.bubble.css'
    
    import { quillEditor } from 'vue-quill-editor'
    
    export default {
      components: {
        quillEditor
      }
    }
    ```

* 使用

  * ~~~
    <quill-editor></quill-editor>
    ~~~

  * 修改样式，通过查看器找到class="quill-editor"，复写

    ~~~
    .quill-editor {
      min-height: 300px;
    }
    ~~~

* 图片放大缩小拖拽

  * https://www.cnblogs.com/zr123/p/12206031.html
  * https://segmentfault.com/a/1190000021610181
  
  

## 富文本 tinymce

* https://www.cnblogs.com/yubingyang/p/11561517.html



## 富文本 wangEditor 

* https://zhuanlan.zhihu.com/p/43416702

* https://www.wangeditor.com/index.html

* 组件用法（不好用）

  * 新建wangEditor.vue
    https://github.com/wangeditor-team/wangEdior-with-vue/blob/master/src/views/Home.vue

  * 需要保存本地图片为base64：
    	通过文档 https://doc.wangeditor.com/pages/07-%E4%B8%8A%E4%BC%A0%E5%9B%BE%E7%89%87/12-base64%E4%BF%9D%E5%AD%98%E5%9B%BE%E7%89%87.html 得知，设置：
    	editor.config.uploadImgShowBase64 = true

  * 使用：
    	import vueWangeditor from '../wangEditor/WangEditor'

    ​	components: { vueWangeditor },

     	<vue-wangeditor id="editor" v-model="text"></vue-wangeditor>

* npm插件 vue-wangeditor

  * https://www.npmjs.com/package/vue-wangeditor



##  富文本 ueditor

* https://github.com/HaoChuan9421/vue-ueditor-wrap  

* https://www.npmjs.com/package/vue-ueditor-wrap

  ~~~
  可以集成了，确实比原来的更像传统编辑器。但是他妈的最基本的插入图片，居然不支持python后台。
  为了插图片还得再撘个php、java后台啥的，要么就得自己开发个插入图片的插件，把图片转换成base64再插入，再开发一个支持拖拽和缩放的插件。果断放弃。
  ~~~

  





## 上传下载文件

* https://www.cnblogs.com/zhang-can/p/9116159.html

* https://www.jb51.net/article/190562.htm

* 下载用`js-file-download`

* https://segmentfault.com/a/1190000020540788

  

## 页面滚动到指定位置

* https://developer.mozilla.org/zh-CN/docs/Web/API/Element/scrollIntoView

* ```
  setTimeout(() => {
          document.getElementById("id-el-card-info").scrollIntoView({ behavior: "smooth" })
        }, 500);
  ```

* 使用settimeout，否则加载慢的页面没有效果

* 

## vue 图形验证vue2-verify

* https://github.com/mizuka-wu/vue2-verify

* ```
  npm install vue2-verify
  ```



## 报错 'webpack-dev-server' 不是内部或外部命令，也不是可运行的程序

* 项目目录下：
*  npm install;
* npm run build;
* npm run dev



## elementUi 菜单激活的问题

~~~
:default-active="$route.path.slice(1)"
因为$route.path返回值为"/customerAdd"，而 el-menu 的 index 不带"/" ,所以必须用slice处理
~~~

# js跨域问题
https://blog.csdn.net/wh_xmy/article/details/87705840
* main.js
  * 注释 axios.defaults.baseURL = 'http://39.99.231.153:8000/api/'
  * baseUrl不在这里写，而是写到配置代理表里
  ~~~
  axios.defaults.baseURL = '/api'
  ~~~
* config/index.js
  ~~~
  proxyTable: {
      '/api': {
        target:'http://39.99.231.153:8000/api/', // 你请求的第三方接口
        changeOrigin:true, // 在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
        pathRewrite:{  // 路径重写，
          '^/api': ''  // 替换target中的请求地址，也就是说以后你在请求http://api.douban.com/v2/XXXXX这个地址的时候直接写成/api即可。
        }
      },
    },
  ~~~