import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/home/Home'
import Hei from '@/components/Hei'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/hei',
      name: 'Hei',
      component: Hei
    }
  ]
})
