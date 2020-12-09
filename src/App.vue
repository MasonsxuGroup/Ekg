<template>
  <div id="app">
    <router-view />
    <!-- <Home></Home> -->
  </div>
</template>

<script>
import Home from "./components/Home";
export default {
  name: "App",
  components: { Home },
};
</script>

<style>
body {
  margin: 0;
}
* {
  overflow-x: hidden;
}
#app {
  width: 100%;
  height: 100%;
}
</style>
