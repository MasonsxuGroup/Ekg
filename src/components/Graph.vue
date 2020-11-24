<template>
  <div id="graph">
    <el-row id="up-row">
      <i class="el-icon-s-home" style="display: inline-block"></i>
      <span style="display: inline-block">图谱预览</span>
      <div id="up-row-input" style="display: inline-block">
        <el-input
          size="small"
          placeholder="请输入内容"
          prefix-icon="el-icon-search"
          v-model="inputEntity"
          style="width: 535px"
        >
        </el-input>
      </div>
    </el-row>
    <el-row id="dowm-row">
      <EchartsGraph :text='inputEntity'></EchartsGraph>
    </el-row>
  </div>
</template>

<script>
import EchartsGraph from "./EchartsGraph";
export default {
  name: "graph",
  data() {
    return {
      inputEntity: "",
    };
  },
  components: { EchartsGraph },
  methods: {},
};
</script>

<style lang="scss" scoped>
#up-row {
  margin-bottom: 15px;
  height: 60px;
  line-height: 60px;
  text-align: left;
  padding-left: 20px;
  background-color: rgba(138, 148, 155, 0.2);
}
#dowm-row {
  height: 400px;
  border: 1px solid rgba(138, 148, 155, 0.2);
}
</style>