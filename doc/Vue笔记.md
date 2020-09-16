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
    啰嗦，直接传数组
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
    父子传值： 类似于变量的使用过程1、声明 2、赋值  3、使用
    1、声明：c-c子组件中 props:['a']  
    2、赋值：<c-c :a="msg"></c-c>   也就是绑定父组件的msg
    3、使用：c-c的template中像data一样使用

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

# 一键vue模板
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

# 项目使用axios
npm i axios
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
