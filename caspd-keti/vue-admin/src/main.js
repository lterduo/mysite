// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
// 导入全局样式
import './assets/base.css'
import 'element-ui/lib/theme-chalk/index.css';
//axios
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
Vue.prototype.axios = axios

Vue.config.productionTip = false

Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
