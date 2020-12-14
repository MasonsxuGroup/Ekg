import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    ruleForm: {
      content:
        "青岛新增3例新冠无症状感染者，北京10月10日无新增报告新冠肺炎确诊病例10月10日0时至24时，无新增报告本地确诊病例、疑似病例和无症状感染者；无新增报告境外输入确诊病例、疑似病例和无症状感染者。"
    }
  }
});
