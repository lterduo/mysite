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
import ProjectAssessAdmin from '../components/project/ProjectAssessAdmin.vue'

Vue.use(Router)

const router = new Router({
  mode:'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/',
      name: '/',
      component: Home
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
        },{
          path:'/projectAssessAdmin',
          name:'projectAssessAdmin',
          component: ProjectAssessAdmin
        }
      ]
    },
    
  ]
})

// 挂载路由导航守卫,to表示将要访问的路径，from表示从哪里来，next是下一个要做的操作 next('/login')强制跳转login
router.beforeEach((to, from, next) => {
  // 访问登录页，放行
  if (to.path === '/login') return next()
  // 获取token
  const tokenStr = localStorage.getItem('token')
  // 没有token, 强制跳转到登录页
  if (!tokenStr){
     return next('/login')
  }

  //如果手动输入地址，要检验是否在权限菜单列表中。不在menus里，强制跳转
  const menus = JSON.parse(localStorage.getItem("menus"))
  let ml = ['/home','/login','/']
  menus.data.forEach(item=>{

    item.children.forEach(itemSub=>{
      ml.push('/' + itemSub.path)
    })
  })
  const menuList = ml

  if(menuList.includes(to.path)){
    next()
  }else{
    alert('没有权限')
    next('/login')
  }

})

export default router

