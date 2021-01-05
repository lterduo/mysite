import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

Vue.prototype.$baseUrl = 'http://39.99.231.153:8000'

App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()
