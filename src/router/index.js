import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import EchartsGraph from "../components/EchartsGraph.vue";
import Recognition from "../components/Recognition.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "根路由",
      redirect: "/home",
      show: false
    },
    {
      path: "/home",
      name: "突发事件",
      component: Home,
      redirect: "/recognition",
      show: true,
      children: [
        {
          path: "/recognition",
          name: "实体识别",
          component: Recognition,
          show: true
        },
        {
          path: "/graph",
          name: "图谱预览",
          component: EchartsGraph,
          show: true
        }
      ]
    }
  ]
});
