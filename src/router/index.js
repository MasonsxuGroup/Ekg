import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import Graph from "../components/Graph.vue";
import Recognition from "../components/Recognition.vue";

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/",
      name: "突发事件",
      component: Home,
      redirect: "/recognition",
      children: [
        {
          path: "/recognition",
          name: "实体识别",
          component: Recognition
        },
        {
          path: "/graph",
          name: "图谱预览",
          component: Graph
        }
      ]
    }
  ]
});
