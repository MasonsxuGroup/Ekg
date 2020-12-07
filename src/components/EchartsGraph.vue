<template>
  <div id="graph-chart">
    <div id="main-chart" style="width: 100%; height: 100%"></div>
  </div>
</template>

<script>
// import bus from '../../static/js/eventBus'
import echarts from "echarts";

export default {
  name: "graph-echart",
  props: ["text"],
  data() {
    return {
      graph_data: {},
    };
  },
  mounted() {
    // this.bus.$on('sendData',(data)=>{
    //   console.log(res)
    // })
    // this.fetchData();
    this.initChart();
    // this.test()
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData: function () {
      this.axios
        .get("api/figure")
        .then((res) => {
          let resp = res.data.data;
          this.graph_data["node"] = [];
          this.graph_data["links"] = [];
          for (let i in resp) {
            let source = "";
            let node_dict = {};
            let links_dict = {};
            source = resp[i]["LOC"];
            node_dict["name"] = resp[i]["LOC"];
            node_dict["category"] = 0; //0=>LOC
            this.graph_data["node"].push(node_dict);
            for (let k in resp[i]["TIME"]) {
              let node_dict = {};
              let links_dict = {};
              node_dict["name"] = resp[i]["TIME"][k];
              node_dict["category"] = 1; //1=>TIME
              links_dict["source"] = source;
              links_dict["target"] = resp[i]["TIME"][k];
              links_dict["name"] = "时间";
              this.graph_data["node"].push(node_dict);
              this.graph_data["links"].push(links_dict);
            }
            for (let k in resp[i]["RES"]) {
              let node_dict = {};
              let links_dict = {};
              node_dict["name"] = resp[i]["RES"][k];
              node_dict["category"] = 2; //2=>RES
              links_dict["source"] = source;
              links_dict["target"] = resp[i]["RES"][k];
              links_dict["name"] = "结果";
              this.graph_data["node"].push(node_dict);
              this.graph_data["links"].push(links_dict);
            }
          }
          console.log(this.graph_data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    initChart: function () {
      let myChart = echarts.init(document.getElementById("main-chart"));
      myChart.resize();
      myChart.setOption(this.setOption());
    },
    setOption: function () {
      console.log(this.graph_data);
      let option = {
        title: {
          text: "Graph 简单示例",
        },
        tooltip: { formatter: "{b}" }, //提示框
        animationDurationUpdate: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            type: "graph",
            layout: "force",
            // symbolSize: 50, //倘若该属性不在link里，则其表示节点的大小；否则即为线两端标记的大小
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
              }
            },
            roam: true, //鼠标缩放功能
            label: {
              show: true, //是否显示标签
            },
            focusNodeAdjacency: true, //鼠标移到节点上时突出显示结点以及邻节点和边
            edgeSymbol: ["none", "none"], //关系两边的展现形式，也即图中线两端的展现形式。arrow为箭头
            edgeSymbolSize: [4, 10],
            draggable: true,
            edgeLabel: {
              fontSize: 20, //关系（也即线）上的标签字体大小
            },
            force: {
              repulsion: 500,
              edgeLength: 120,
            },
            data: this.graph_data["node"],
            // links: this.graph_data["links"],
            lineStyle: {
              opacity: 0.9,
              width: 2,
              curveness: 0,
            },
          },
        ],
      };
      return option;
    },
  },
};
</script>

<style lang="scss" scoped>
#graph-chart {
  height: 100%;
  width: 100%;
}
</style>