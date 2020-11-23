<template>
  <div id="home">
    <el-container style="height: 700px; border: 1px solid #eee">
      <el-aside width="250px" style="background-color: rgb(238, 241, 246)">
        <el-menu>
          <el-submenu index="1">
            <template slot="title"
              ><i class="el-icon-s-unfold"></i>突发事件</template
            >
            <el-submenu index="1-1">
              <template slot="title"
                ><i class="el-icon-s-unfold"></i>公共卫生</template
              >
              <!-- <el-menu-item index="1-1-1">新冠肺炎</el-menu-item> -->
              <el-submenu index="1-1-1">
                <template slot="title"
                  ><i class="el-icon-s-unfold"></i>甲类传染病</template
                >
                <!-- <el-menu-item index="1-1-1">新冠肺炎</el-menu-item> -->
                <el-submenu index="1-1-1-1" :default-openeds="['1']">
                  <template slot="title"
                    ><i class="el-icon-menu"></i>新冠肺炎</template
                  >
                  <!-- <el-menu-item index="1-1-1">新冠肺炎</el-menu-item> -->
                  <el-submenu
                    v-for="(province, index) in provinces"
                    :key="'P' + index"
                    :index="'1-1-1-1' + (index + 1) + ''"
                  >
                    <template slot="title"
                      ><i class="el-icon-location-outline"></i
                      >{{ province }}</template
                    >
                    <template v-for="city in cities" v-if="city.n == province">
                      <el-menu-item
                        class="el-icon-place"
                        v-for="(item, index2) in city.cities"
                        :key="'C' + index2"
                        :index="'1-1-1-1-' + index + '-' + index2 + ''"
                        @click="clickMenuItem(item.n, $event)"
                        >{{ item.n }}</el-menu-item
                      >
                    </template>
                  </el-submenu>
                </el-submenu>
              </el-submenu>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-row>
            <el-input
              class="home-search"
              style="float: left; width: 200px; border-radius: 5px 0 0 5px"
              placeholder="请输入内容"
              v-model="input"
              clickMenuItem
            >
            {{input}}
            </el-input>
            <!-- <el-button style="float:left" type="primary">主要按钮</el-button> -->
            <el-button id="home-btn" icon="el-icon-search" circle></el-button>
          </el-row>
        </el-header>

        <el-main>
          <!-- <router-view></router-view> -->
          <Graph :text='input'></Graph>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Graph from "../components/Graph";
export default {
  name: "home",
  data() {
    return {
      input: "",
      provinces: [],
      cities: [],
    };
  },
  components: { Graph },
  methods: {
    getNavData: function () {
      const _this = this;
      this.axios.get("../../static/data/cities.json").then(function (res) {
        if (res.status == 200) {
          // _this.cities = res.data;
          let navData = res.data;
          // let cityData = [];
          let i;
          let j;
          for (i in navData) {
            // _this.cities = navData[i]
            // console.log(navData[i])
            for (j in navData[i]) {
              // console.log(navData[i][j])
              let navDataItems = navData[i][j];
              _this.provinces.push(navDataItems["n"]);
              // console.log(navDataItems['cities'])
              //hasOwnProperty()判断对象是否含有某属性（key值）
              if (navDataItems.hasOwnProperty("cities")) {
                _this.cities.push(navDataItems);
              }
            }
          }
        } else {
          console.log("cities数据未读入！");
        }
      });
    },
    clickMenuItem: function(name,event){
      this.input = name
    },
  },
  mounted() {
    this.getNavData();
  },
};
</script>

<style scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
.el-input {
  display: block;
}
/*if you want to cover the style of elementUI's componets, you'd better add a classname wo your tags.
then modify the style like this*/
.home-search >>> .el-input__inner {
  border-radius: 5px 0px 0px 5px;
}
#home-btn {
  float: left;
  margin: 11px 0 3px 0px !important;
  border-radius: 0 50% 50% 0;
}
</style>