<template>
  <div id="app">
    <!-- <router-view/> -->
    <!-- <test></test> -->
    <Home></Home>
  </div>
</template>

<script>
import Test from './components/Test'
import Home from './components/Home'
export default {
  name: 'App',
  components:{Home,Test}
}
</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
