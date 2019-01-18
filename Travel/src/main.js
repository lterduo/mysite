// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router' //./router/index.js 配置中写了，会自动找几个默认文件
import store from './store'
import fastClick from 'fastclick'
import './assets/styles/reset.css'
import './assets/styles/iconfont.css'
import 'styles/border.css'
import VueAwesomeSwiper from 'vue-awesome-swiper'

// require styles
import 'swiper/dist/css/swiper.css'

Vue.config.productionTip = false
fastClick.attach(document.body) 
Vue.use(VueAwesomeSwiper, /* { default global options } */)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router, 
  store,  //store: store 
  components: { App },
  template: '<App/>'
})
