import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import Graph from "../components/Graph.vue";
import Recognition from "../components/Recognition.vue";
import Login from '../components/Login.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path:'/',
      name:'跟路由',
      redirect:'/login',
      show:false
    },
    {
        path:'/login',
        name:'用户登录',
        component:Login,
        show:false
    },
    {
      path: "/home",
      name: "突发事件",
      component: Home,
      redirect: "/recognition",
      show:true,
      children: [
        {
          path: "/recognition",
          name: "实体识别",
          component: Recognition,
          show:true,
        },
        {
          path: "/graph",
          name: "图谱预览",
          component: Graph,
          show:true,
        }
      ]
    }
  ]
});
