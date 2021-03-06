// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/css/base.css'

import moment from 'moment'

import axios from 'axios'
// axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
Vue.prototype.axios = axios

Vue.use(ElementUI)

Vue.config.productionTip = false

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
