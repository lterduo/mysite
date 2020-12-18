import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/login/Login.vue'
import Home from '../components/home/Home.vue'
import HomeMain from '../components/home/HomeMain.vue'


import CustomerAdd from '../components/customer/CustomerAdd.vue'
import CustomerImg from '../components/customer/CustomerImg.vue'



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      children:[
        {
          path: '/',
          name: 'homeMain',
          component: HomeMain
        },
        {
          path: '/customerAdd',
          name: 'customerAdd',
          component: CustomerAdd
        },
        {
          path: '/customerImg',
          name: 'customerImg',
          component: CustomerImg
        },
      ]
    },
    
  ]
})
