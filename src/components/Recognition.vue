<template>
  <div id="entity-reco">
    <el-row id="top-row">
      <i class="el-icon-s-home"></i>
      <span>实体识别</span>
    </el-row>
    <el-row id="mid-row">
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
        <p id="mid-form-label">输入信息</p>
        <div style="padding: 0 15px">
          <el-form-item prop="content">
            <el-input
              type="textarea"
              v-model="ruleForm.content"
              rows="4"
              style="border-style: ridge"
              maxlength="150"
              show-word-limit
            ></el-input>
            <el-form-item style="margin-top: 10px">
              <el-button type="primary" @click="submitForm('ruleForm')"
                >提交</el-button
              >
              <el-button @click="resetForm">重置</el-button>
            </el-form-item>
          </el-form-item>
        </div>
      </el-form>
    </el-row>
    <el-row id="bottom-row">
      <p id="btm-form-label">识别结果</p>
      <div
        style="
          padding: 0 15px;
          border-style: grrove;
          height: 160px;
          display: flex;
          flex-wrap: wrap;
        "
      >
        <div
          id="output-result"
          v-for="(entity, index) in entities"
          @mouseover="onMouseOver(index)"
          @mouseleave="onMouseLeave"
          :class="{ activeClass: index === isActive }"
          :title="resp_values[index]"
        >
          <!-- <span id="promptBox" v-if="seen">{{resp_values[index]}}</span> -->
          <p
            style="
              margin: 0;
              line-height: 30px;
              font-weight: 580;
              padding: 0 16px;
            "
          >
            {{ entity }}
          </p>
          <p
            style="
              margin: 0;
              line-height: 20px;
              font-size: 12px;
              padding: 0 16px;
            "
          >
            {{ resp_values[index] }}
          </p>
        </div>
      </div>
    </el-row>
  </div>
</template>

<script>
// import bus from '../../static/js/eventBus'
export default {
  data() {
    return {
      isActive: "",
      // seen: false,
      ruleForm: {
        content:
          "青岛新增3例新冠无症状感染者，北京10月10日无新增报告新冠肺炎确诊病例10月10日0时至24时，无新增报告本地确诊病例、疑似病例和无症状感染者；无新增报告境外输入确诊病例、疑似病例和无症状感染者。",
      },
      rules: {
        content: [
          { required: true, message: "输入内容不能为空！", trigger: "blur" },
          {
            min: 0,
            max: 150,
            message: "输入字符不得超过150个字符",
            trigger: "blur",
          },
        ],
      },
      entities: [],
      resp_values: [],
      result: "",
    };
  },
  methods: {
    submitForm(formName) {
      const _this = this;
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.axios
            .post("/api/extract", this.ruleForm)
            .then(function (res) {
              let resp = res.data.data;
              let temp = [];
              let value_temp = [];
              if (res.status == 200) {
                for (let i in resp) {
                  temp.push(String(resp[i]['item']));
                  _this.entities = temp;
                  value_temp.push(String(resp[i]['pos']));
                  _this.resp_values = value_temp;
                }
              }
            })
            .catch((error) => console.log(error));
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm: function () {
      this.ruleForm.content = "";
    },
    onMouseOver: function (index) {
      this.isActive = index;
    },
    onMouseLeave: function () {
      this.isActive = "";
    },
  },
  created() {},
  mounted() {},
};
</script>

<style lang="scss" scoped>
#top-row {
  margin-bottom: 15px;
  height: 60px;
  line-height: 60px;
  text-align: left;
  padding-left: 20px;
  background-color: rgba(138, 148, 155, 0.2);
}

#mid-row {
  height: 200px;
  border: 1px solid rgba(138, 148, 155, 0.2);
  margin-bottom: 15px;
}

#bottom-row {
  height: 250px;
  border: 1px solid rgba(138, 148, 155, 0.2);
}
#mid-form-label,
#btm-form-label {
  height: 20px;
  line-height: 20px;
  text-align: left;
  padding: 0 15px;
  font-weight: 600;
  margin: 10px 0;
}

#output-result {
  // display: inline-block;
  border: 1px solid #e0e0e0;
  border-radius: 4%;
  background-color: white;
  // float: left;
  font-size: 15px;
  margin: 5px;
  height: 48px;
  // line-height: 38px;
}
.activeClass {
  background-color: #409eff !important;
}
#outpu-result p {
  line-height: 20;
  position: relative;
}
</style>