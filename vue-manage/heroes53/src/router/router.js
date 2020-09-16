import Vue from 'vue'
import VueRouter from 'vue-router'

import list from "../components/list/list.vue"
import details from "../components/details/details.vue"
import bar from '../components/bar/bar.vue'

Vue.use(VueRouter)

var routes = [
    { name: '', path: '/list', component: list },
    { name: '', path: '/details', component: details },
    { name: '', path: '/bar', component: bar },
]

var router = new VueRouter({
    routes
})

export default router