import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home.vue";
import Graph from "../components/Graph.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
  ]
});
