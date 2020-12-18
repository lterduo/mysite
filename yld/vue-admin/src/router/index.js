import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/login/Login.vue'
import Home from '../components/home/Home.vue'
import HomeMain from '../components/home/HomeMain.vue'


import CustomerEdit from '../components/customer/CustomerEdit.vue'
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
          path: '/customerEdit',
          name: 'customerEdit',
          component: CustomerEdit
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
