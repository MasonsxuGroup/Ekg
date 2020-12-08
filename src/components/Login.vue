<template>
  <div id="login">
    <h1 @click="pageHome">登陆界面</h1>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {};
  },
  methods: {
    pageHome: function () {
      // console.log(this.$router)
      this.$router.push("/home");
    },
  },
};
</script>

<style lang="scss" scoped>
</style>