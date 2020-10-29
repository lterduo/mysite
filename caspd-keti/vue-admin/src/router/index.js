import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/login/Login.vue'
import Home from '../components/home/Home.vue'
import HomeMain from '../components/home/HomeMain.vue'
import Applicant from '../components/applicant/Applicant.vue'
import Expert from '../components/expert/Expert.vue'
import ProjectCategory from '../components/projectCategory/ProjectCategory.vue'

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
          path: '/applicant',
          name: 'applicant',
          component: Applicant
        },
        {
          path: '/expert',
          name: 'expert',
          component: Expert
        },
        {path:'/projectCategory', name: 'projectCategory', component: ProjectCategory}
      ]
    },
    
  ]
})
