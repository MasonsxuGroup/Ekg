<template>
  <div id="test">
    <div id="myChart"></div>
  </div>
</template>

<style scoped>
#myChart {
  width: 100%;
  height: 100%;
}
</style>

<script>
export default {
  name: "test",
  data() {
    return {};
  },
  methods: {
    datapro: function () {
      let i;
      let dataInfo = {
        TIME: {
          0: "8\u67089\u65e524\u65f6",
          1: "7\u670827\u65e5\u4ee5\u6765",
          2: "8\u67089\u65e524\u65f6",
          3: "8\u67089\u65e5",
          4: "8\u67088\u65e524\u65f6",
          5: "8\u67084\u65e5",
          6: "8\u67087\u65e524\u65f6",
          7: "8\u67087\u65e524\u65f6",
        },
        RES: {  
          0: [
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "47\u4f8b" },
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "2\u4f8b" },
            { LOC: "\u65b0\u7586", m: "592\u4f8b" },
          ],
          1: [{ LOC: "\u5927\u8fde\u5e02", m: "4\u4f8b" }],
          2: [
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "49\u4f8b",
            },
            { LOC: "\u4e0a\u6d77", m: "18\u4f8b" },
            { LOC: "\u5c71\u4e1c", m: "4\u4f8b" },
            { LOC: "\u56db\u5ddd", m: "4\u4f8b" },
            { LOC: "\u5e7f\u4e1c", m: "3\u4f8b" },
            { LOC: "\u9655\u897f", m: "3\u4f8b" },
            { LOC: "\u8fbd\u5b81", m: "2\u4f8b" },
            { LOC: "\u6d59\u6c5f", m: "1\u4f8b" },
            { LOC: "\u65b0\u7586", m: "1\u4f8b" },
            { LOC: "\u4e0a\u6d77", m: "64\u4f8b" },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "802\u4f8b",
            },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "31\u4f8b",
            },
            { LOC: "\u6e2f\u6fb3\u53f0\u5730\u533a", m: "4602\u4f8b" },
            { LOC: "\u9999\u6e2f", m: "4079\u4f8b" },
            { LOC: "\u6fb3\u95e8", m: "46\u4f8b" },
            { LOC: "\u53f0\u6e7e\u5730\u533a", m: "477\u4f8b" },
          ],
          3: [{ LOC: "\u798f\u5dde", m: "1\u4f8b" }],
          4: [
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "23\u4f8b",
            },
            { LOC: "\u5e7f\u4e1c", m: "5\u4f8b" },
            { LOC: "\u4e0a\u6d77", m: "2\u4f8b" },
            { LOC: "\u6d59\u6c5f", m: "1\u4f8b" },
            { LOC: "\u65b0\u7586", m: "45\u4f8b" },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "817\u4f8b",
            },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "11\u4f8b",
            },
            { LOC: "\u6e2f\u6fb3\u53f0\u5730\u533a", m: "4530\u4f8b" },
            { LOC: "\u9999\u6e2f", m: "4007\u4f8b" },
            { LOC: "\u6fb3\u95e8", m: "46\u4f8b" },
            { LOC: "\u53f0\u6e7e\u5730\u533a", m: "477\u4f8b" },
          ],
          5: [{ LOC: "\u4e4c\u9c81\u6728\u9f50", m: "637\u4f8b" }],
          6: [
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "28\u4f8b" },
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "2\u4f8b" },
            { LOC: "\u65b0\u7586", m: "640\u4f8b" },
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "637\u4f8b" },
            { LOC: "\u5580\u4ec0\u5730\u533a", m: "1\u4f8b" },
            { LOC: "\u660c\u5409\u5dde", m: "1\u4f8b" },
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "1\u4f8b" },
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "126\u4f8b" },
            { LOC: "\u660c\u5409\u5dde", m: "1\u4f8b" },
            { LOC: "\u4e4c\u9c81\u6728\u9f50\u5e02", m: "108\u4f8b" },
          ],
          7: [
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "31\u4f8b",
            },
            { LOC: "\u4e0a\u6d77", m: "2\u4f8b" },
            { LOC: "\u6d59\u6c5f", m: "1\u4f8b" },
            { LOC: "\u5c71\u4e1c", m: "1\u4f8b" },
            { LOC: "\u6e56\u5317", m: "1\u4f8b" },
            { LOC: "\u5e7f\u4e1c", m: "1\u4f8b" },
            { LOC: "\u65b0\u7586", m: "5\u4f8b" },
            { LOC: "\u4e0a\u6d77", m: "35\u4f8b" },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "839\u4f8b",
            },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "14\u4f8b",
            },
            { LOC: "\u6e2f\u6fb3\u53f0\u5730\u533a", m: "4461\u4f8b" },
            { LOC: "\u9999\u6e2f", m: "3938\u4f8b" },
            { LOC: "\u6fb3\u95e8", m: "46\u4f8b" },
            { LOC: "\u53f0\u6e7e\u5730\u533a", m: "477\u4f8b" },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "31\u4f8b",
            },
            { LOC: "\u4e0a\u6d77", m: "2\u4f8b" },
            { LOC: "\u6d59\u6c5f", m: "1\u4f8b" },
            { LOC: "\u5c71\u4e1c", m: "1\u4f8b" },
            { LOC: "\u6e56\u5317", m: "1\u4f8b" },
            { LOC: "\u5e7f\u4e1c", m: "1\u4f8b" },
            { LOC: "\u65b0\u7586", m: "5\u4f8b" },
            { LOC: "\u4e0a\u6d77", m: "35\u4f8b" },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "839\u4f8b",
            },
            {
              ORG: "\u65b0\u7586\u751f\u4ea7\u5efa\u8bbe\u5175\u56e2",
              m: "14\u4f8b",
            },
            { LOC: "\u6e2f\u6fb3\u53f0\u5730\u533a", m: "4461\u4f8b" },
            { LOC: "\u9999\u6e2f", m: "3938\u4f8b" },
            { LOC: "\u6fb3\u95e8", m: "46\u4f8b" },
            { LOC: "\u53f0\u6e7e\u5730\u533a", m: "477\u4f8b" },
          ],
        },
      };
      
      for (i in dataInfo['RES']) {
        console.log(dataInfo[i]);
        // dataInfo[]
      }
    },
    drawGraph: function () {
      let myChart = this.$echarts.init(document.getElementById("myChart"));

      myChart.setOption({
        title: {
          text: "实体属性关系图",
          top: "top",
          left: "center",
        },
        itemStyle: {
          normal: {
            color: "#000",
          },
          shadowBlur: 10,
        },
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        xAxis: {
          show: false,
          type: "value",
        },
        yAxis: {
          show: false,
          type: "value",
        },
        series: [
          {
            type: "graph",
            coordinateSystem: "cartesian2d",
            legendHoverLink: false,
            hoverAnimation: true,
            nodeScaleRatio: false,
            //建头
            edgeSymbol: ["circle", "arrow"],
            edgeSymbolSize: [2, 15],
            edgeLabel: {
              show: false,
              normal: {
                show: true,
                position: "middle",
                textStyle: {
                  fontSize: 12,
                },
                formatter: "{c}",
              },
            },
            focusNodeAdjacency: true,
            roam: true,
            categories: [
              {
                name: "一级关系",
                itemStyle: {
                  //可配置颜色
                  normal: {
                    color: "#A170DD",
                  },
                },
              },
              {
                name: "二级关系",
                itemStyle: {
                  //可配置颜色
                  normal: {
                    color: "#41B1EF",
                  },
                },
              },
              {
                name: "三级关系",
                itemStyle: {
                  //可配置颜色
                  normal: {
                    color: "#E8B842",
                  },
                },
              },
              {
                name: "四级关系",
                itemStyle: {
                  //可配置颜色
                  normal: {
                    color: "#667AED",
                  },
                },
              },
            ],
            //圆形上面的文字
            label: {
              normal: {
                position: "inside",
                show: true,
                textStyle: {
                  color: "#fff",
                  fontSize: 12,
                },
              },
            },
            force: {
              repulsion: 1000,
            },
            force: {
              repulsion: 2500,
            },
            itemStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  {
                    offset: 0,
                    color: "#157eff",
                  },
                  {
                    offset: 1,
                    color: "#35c2ff",
                  },
                ]),
              },
              shadowBlur: 10,
            },
            // lineStyle: {
            //     normal: {
            //         width: 1,
            //         shadowColor: 'none',
            //         color: '#0250FD'
            //     },
            // },
            lineStyle: {
              normal: {
                opacity: 0.9,
                width: 1,
                curveness: 0.1,
              },
            },
            data: dataInfo,
            // links: dataLink,
          },
        ],
      });
    },
  },
  mounted() {
    this.datapro();
  },
};
</script>