<template>
  <div id="graph-chart">
    <div id="main-chart" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
//引入基本模板
let echarts = require("echarts/lib/echarts");

//引入图形类型
require("echarts/lib/chart/graph");

//引入使用组件title、tooltip等
require("echarts/lib/component/title");
require("echarts/lib/component/tooltip");

export default {
  name: "graph-echart",
  // props: ["text"],
  data() {
    return {
      graph_data: {},
    };
  },
  mounted() {
    this.fetchData();
  },
  created() {},
  methods: {
    fetchData: function () {
      const _this = this;
      this.axios
        .get("api/figure")
        .then((res) => {
          let resp = res.data.data;
          _this.graph_data["node"] = [];
          _this.graph_data["links"] = [];
          // let num = 0;
          for (let i in resp) {
            let source = "";
            let node_dict = {};
            let links_dict = {};
            if (resp[i]["LOC"].length != 0) {
              source = resp[i]["LOC"];
              // node_dict["id"] = String(num);
              node_dict["name"] = resp[i]["LOC"];
              node_dict["category"] = 0; //0=>LOC
              _this.graph_data["node"].push(node_dict);
            } else {
              source = "全国";
              // node_dict["id"] = String(num);
              node_dict["name"] = "全国";
              node_dict["category"] = 0; //0=>LOC
              _this.graph_data["node"].push(node_dict);
            }
            // num += 1;
            for (let k in resp[i]["TIME"]) {
              let node_dict = {};
              let links_dict = {};
              // node_dict["id"] = String(num);
              node_dict["name"] = resp[i]["TIME"][k];
              node_dict["category"] = 1; //1=>TIME
              links_dict["source"] = source;
              links_dict["target"] = resp[i]["TIME"][k];
              links_dict["name"] = "时间";
              _this.graph_data["node"].push(node_dict);
              _this.graph_data["links"].push(links_dict);
              // num += 1;
            }
            for (let j in resp[i]["RES"]) {
              let node_dict = {};
              let links_dict = {};
              // node_dict["id"] = String(num);
              node_dict["name"] = resp[i]["RES"][j];
              node_dict["category"] = 2; //2=>RES
              links_dict["source"] = source;
              links_dict["target"] = resp[i]["RES"][j];
              links_dict["name"] = "结果";
              _this.graph_data["node"].push(node_dict);
              _this.graph_data["links"].push(links_dict);
              // num += 1;
            }
            for (let k in resp[i]["PER"]) {
              let node_dict = {};
              let links_dict = {};
              // node_dict["id"] = String(num);
              node_dict["name"] = resp[i]["PER"][k];
              node_dict["category"] = 3; //1=>TIME
              links_dict["source"] = source;
              links_dict["target"] = resp[i]["PER"][k];
              links_dict["name"] = "人物";
              _this.graph_data["node"].push(node_dict);
              _this.graph_data["links"].push(links_dict);
              // num += 1;
            }
            for (let k in resp[i]["ORG"]) {
              let node_dict = {};
              let links_dict = {};
              // node_dict["id"] = String(num);
              node_dict["name"] = resp[i]["ORG"][k];
              node_dict["category"] = 4; //1=>TIME
              links_dict["source"] = source;
              links_dict["target"] = resp[i]["ORG"][k];
              links_dict["name"] = "机构";
              _this.graph_data["node"].push(node_dict);
              _this.graph_data["links"].push(links_dict);
              // num += 1;
            }
          }
          _this.initChart();
          // console.log(this.graph_data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    initChart: function () {
      let myChart = echarts.init(document.getElementById("main-chart"));
      let option = {
        title: {
          text: "图谱展示",
        },
        tooltip: { formatter: "{b}" }, //提示框
        animationDurationUpdate: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            type: "graph",
            layout: "force",
            symbolSize: (value, params) => {
              switch (params.data.category) {
                case 0:
                  return 100;
                  break;
                case 1:
                  return 75;
                  break;
                case 2:
                  return 75;
                  break;
                case 3:
                  return 75;
                  break;
                case 4:
                  return 75;
                  break;
              }
            },
            roam: true, //鼠标缩放功能
            label: {
              show: true, //是否显示标签
              color: "#fff",
            },
            itemStyle: {
              color: function (params, value) {
                // console.log(value);
                switch (params.data.category) {
                  case 0:
                    return "#0e1f37";
                    break;
                  case 1:
                    return "#8d776e";
                    break;
                  case 2:
                    return "#f45249";
                    break;
                  case 3:
                    return "#1b4a58";
                    break;
                  case 4:
                    return "#66a4ac";
                    break;
                }
              },
            },
            focusNodeAdjacency: true, //鼠标移到节点上时突出显示结点以及邻节点和边
            edgeSymbol: ["none", "none"], //关系两边的展现形式，也即图中线两端的展现形式。arrow为箭头
            edgeSymbolSize: [4, 10],
            draggable: true,
            edgeLabel: {
              normal: {
                show: true,
                //通过回调函数设置连线上的标签
                formatter: function (x) {
                  return x.data.name;
                },
              },
            },
            force: {
              repulsion: 200,
              edgeLength: [50, 200],
              gravity: 0.05,
            },
            data: this.graph_data.node,
            links: this.graph_data.links,
            lineStyle: {
              opacity: 0.9,
              color: "#000",
              width: 1,
              curveness: 0.5,
            },
          },
        ],
      };
      myChart.resize();
      myChart.setOption(option);
    },
  },
};
</script>

<style lang="scss" scoped>
#graph-chart {
  height: 100%;
  width: 100%;
  border: 1px solid rgba(138, 148, 155, 0.2);
}
</style>