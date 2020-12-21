import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/login/Login.vue'
import Home from '../components/home/Home.vue'
import HomeMain from '../components/home/HomeMain.vue'
import Applicant from '../components/applicant/Applicant.vue'
import Expert from '../components/expert/Expert.vue'
import ProjectCategory from '../components/projectCategory/ProjectCategory.vue'
import ProjectAdd from '../components/project/ProjectAdd.vue'
import ProjectAudit from '../components/project/ProjectAudit'
import ProjectAssess from '../components/project/ProjectAssess.vue'
import ProjectDistribute from '../components/project/ProjectDistribute'


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
        {
          path:'/projectCategory', 
          name: 'projectCategory', 
          component: ProjectCategory
        },
        {
          path: '/projectAdd',
          name: 'projectAdd',
          component: ProjectAdd
        },
        {
          path: '/projectAudit',
          name: 'projectAudit',
          component: ProjectAudit
        },{
          path:'/projectAssess',
          name:'projectAssess',
          component: ProjectAssess
        },{
          path:'/projectDistribute',
          name:'projectDistribute',
          component: ProjectDistribute
        }
      ]
    },
    
  ]
})