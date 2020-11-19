<template>
  <div>
    <div class="select">
      <div>
        <div>课题类别</div>
        <el-select v-model="category" @change="changeCategory" filterable allow-create default-first-option
          placeholder="请选择课题类别">
          <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
          </el-option>
        </el-select>
      </div>
      <div class="space"></div>
      <div>
        <div>评审专家</div>
        <el-select v-model="assessor" @change="changeAssessor" filterable allow-create default-first-option
          placeholder="请选择专家">
          <el-option v-for="item in assessors" :key="item.userid" :label="item.username" :value="item.userid">
          </el-option>
        </el-select>
      </div>
    </div>
    <div>{{category}}</div>
    <div>{{assessor}}</div>
    <!-- 课题分配穿梭框 -->
    <div class="data">
      <el-table :data="data1" style="width: 100%">
        <el-table-column prop="pname" label="课题名称" width="200">
        </el-table-column>
        <el-table-column prop="date" label="操作" width="50">
        </el-table-column>
      </el-table>
      <el-table :data="data1" style="width: 100%">
        <el-table-column prop="date" label="日期" width="180">
        </el-table-column>
      </el-table>
    </div>
    <div>value1: {{value1}}</div>
    <div>data1: {{data1}}</div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      data1:  //
        [],
      value1: [],
      category: '',
      assessor: '',
      projectCategorys: [], //课题类别列表
      assessors: [],  //专家列表
      projectDistribute: [],  //分配信息
    }
  },
  created () {
    this.getProjectCategorys()
    this.getAssessor()
  },
  methods: {

    // 获取课题类型
    async getProjectCategorys () {
      const res = await this.axios.get(`/projectCategory/`)
      if (res.status === 200) {
        this.projectCategorys = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    //获取专家列表
    async getAssessor () {
      let res = await this.axios.get(`/user/?role_id=3`)
      if (res.status === 200) {
        this.assessors = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },
    // 课题改变时改变穿梭框
    async changeCategory () {
      this.data1 = []
      try {
        let res = await this.axios.get(`/projectInfo/?category=${this.category}`)
        this.data1 = res.data.results
      } catch (err) {
        console.log(err)
      }
    },
    //专家改变时将结果读入穿梭框
    async changeAssessor () {

    },
  }
}
</script>

<style lang='less'>
.select {
  display: flex;
  .space {
    width: 100px;
  }
}

.data {
  display: flex;
  margin-top: 20px;
}
</style>