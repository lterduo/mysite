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
import moment from 'moment'


// axios.defaults.baseURL = 'http://39.99.231.153:8000/api/'
axios.defaults.baseURL = '/api'
Vue.prototype.axios = axios

Vue.config.productionTip = false

Vue.use(ElementUI);

// 过滤器
Vue.filter('fmtdate', (v) => {
  return moment(v).format('YYYY-MM-DD')
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
