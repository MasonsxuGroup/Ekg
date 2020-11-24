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
            ></el-input>
            <el-form-item style="margin-top: 10px">
              <el-button type="primary" @click="submitForm('ruleForm')"
                >提交</el-button
              >
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form-item>
        </div>
      </el-form>
    </el-row>
    <el-row id="bottom-row">
      <p id="btm-form-label">识别结果</p>
      <div style="padding: 0 15px">
        <el-input
          type="textarea"
          rows="4"
          placeholder="请输入内容"
          :value="entity"
          readonly
          style="bottom: 65px; border-style: groove"
        >
        </el-input>
      </div>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ruleForm: {
        content: "",
      },
      rules: {
        content: [
          {
            min: 0,
            max: 150,
            message: "输入字符不得超过150个字符",
            trigger: "blur",
          },
        ],
      },
      entity: "测试",
    };
  },
  methods: {
    submitForm(formName) {
      const _this = this;
      this.$refs[formName].validate((valid) => {
        if (valid) {
          //   alert("submit!");
          this.axios
            .post(
              "http://rap2api.taobao.org/app/mock/271582/model/input",
              this.resetForm
            )
            .then(function (res) {
                if(res.status == 200){
                    alert("提交成功！！！")
                }
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    getEnrity: function(){
        const _this = this;
        this.axios.get('http://rap2api.taobao.org/app/mock/271582/model/output').then(function(res){
            // console.log(res)
            let resp = res.data.entities
            let entityStr = ''
            for(let i in resp){
                for(let k in resp[i]){
                    entityStr += resp[i][k] + ' '
                }
            }
            // console.log(entityStr)
            _this.entity = entityStr
            // console.log(typeof(resp))
        })
    },
  },
  created(){
      this.getEnrity()
  }
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
  height: 200px;
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
</style>