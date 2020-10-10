import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/login/login'
import Home from '../components/home/home'
import Users from '../components/users/users.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      name: 'login', path: '/', component: Login
    },
    {
      name: 'home', path: '/home', component: Home,
      children: [
        { name: 'users', path: '/users', component: Users }
      ]
    }
  ]
})
