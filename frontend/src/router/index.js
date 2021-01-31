import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const routes = [
  {
    path: '/index',
    name: 'home',
    component: () => import('../views/Home')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/profile')
  },
  {
    path:'/videoTrans',
    name:'videoTrans',
    component: () => import('../views/Start')
  },
  {
    path:'/play',
    name:'play',
    component: () => import('../views/play')
  },
  {
    path: '*',
    name: '404',
    component: () => import('../views/404'),
    meta:{
      title:'页面走丢了'
    }
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
