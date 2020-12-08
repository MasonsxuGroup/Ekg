<template>
  <div id="home">
    <el-container style="height: 600px; border: 1px solid #eee">
      <el-header>
        <span>突发事件知识图谱</span>
        <el-dropdown
          style="float: right; font-size: 12px; right: 145px; height: 30px"
        >
          <i class="el-icon-setting" style="margin-right: 15px"></i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click.native="jump('github')"
              >关于我们</el-dropdown-item
            >
          </el-dropdown-menu>
        </el-dropdown>
        <span style="float: right; text-align: right">{{ user }}</span>
      </el-header>
      <el-container>
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
          <el-menu router :default-openeds="['2']">
            <el-submenu
              v-for="(item, index) in $router.options.routes"
              :key="index + 1"
              :index="index + 1 + ''"
              v-if="item.show"
            >
              <template slot="title"
                ><i class="el-icon-menu"></i>{{ item.name }}</template
              >
              <el-menu-item
                v-for="(item2, index2) in item.children"
                :key="index2 + 1"
                :index="item2.path"
                :class="$route.path == item2.path ? 'is-active' : ''"
              >
                {{ item2.name }}
              </el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-container>
          <el-main>
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: "MasonsxuGroup",
    };
  },
  methods: {
    // getRouter: function () {
    //   var a = this.$router.options.routes;
    //   console.log(a);
    // },
    jump: function (res) {
      if (res == "github") {
        alert("项目地址，欢迎star！");
        window.open("https://github.com/MasonsxuGroup/Ekg");
      }
    },
  },
  mounted() {
    // this.getRouter();
  },
  watch: {
    $route: {
      handler: function (val, oldVal) {
        console.log(val);
      },
      // 深度观察监听
      deep: true,
    },
  },
};
</script>

<style scoped>
.el-header {
  background-color: rgba(36, 55, 67, 1);
  color: rgba(40, 183, 141, 1);
  text-align: left;
  line-height: 60px;
}

.el-aside {
  background-color: rgba(138, 148, 155, 1);
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: rgba(250, 250, 250, 1);
  color: #333;
  text-align: center;
  line-height: 160px;
}
</style>