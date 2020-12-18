<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>申报书分配</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>申报书分配</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <div class="select">
        <div>
          <div style="margin-bottom: 10px;">课题类别:</div>
          <el-select v-model="category" @change="changeCategory" filterable allow-create default-first-option
            placeholder="请选择课题类别" width="400">
            <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
            </el-option>
          </el-select>
        </div>
        <div class="space"></div>
        <div>
          <div style="margin-bottom: 10px;">评审专家:</div>
          <el-select v-model="assessor" @change="changeAssessor" filterable allow-create default-first-option
            placeholder="请选择专家">
            <el-option v-for="item in assessors" :key="item.userid" :label="item.username" :value="item.userid">
            </el-option>
          </el-select>
        </div>
      </div>
      <!-- 课题分配穿梭框 -->
      <div class="data">
        <el-transfer v-model="value" :data="data" @change="changeTransfer" :titles="['课题', '专家']"></el-transfer>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      dataProject: [],
      dataAssessor: [],
      data: [],
      value: [],
      category: '',
      projectCategorys: [], //课题类别列表
      assessor: '',
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
    // 类型改变时改变穿梭框
    async changeCategory () {
      this.data = []
      try {
        // 查询待评审的课题
        let res = await this.axios.get(`/projectInfo/?category=${this.category}&status=4`)
        let info = res.data.results
        for (let i = 0; i < info.length; i++) {
          this.data.push({ key: info[i].pid, label: info[i].name })
        }
      } catch (err) {
        console.log(err)
      }
    },
    //专家改变，穿梭框右侧读入数据
    async changeAssessor () {
      this.value = []
      try {
        let res = await this.axios.get(`/projectDistribute/?assessor=${this.assessor}&category=${this.category}`)
        for (let i = 0; i < res.data.results.length; i++) {
          this.value.push(res.data.results[i].pid)
        }
      } catch (error) {
        console.log(error)
      }
    },
    // 穿梭框按钮
    async changeTransfer (value, direction, movedKeys) {
      // console.log(value, direction, movedKeys);
      // 右边，添加数据
      if (direction == 'right') {
        if (!this.assessor) {
          return this.$message.error('请选择专家')
        }

        for (let i = 0; i < movedKeys.length; i++) {
          let pinfo = this.data.find(item => item.key == movedKeys[i])

          let tempAssessor = this.assessors.find(item => item.userid == this.assessor)
          // console.log(tempAssessor)
          let distribute = { pid: pinfo.key, pname: pinfo.label, category: this.category, assessor: this.assessor, aname: tempAssessor.username }
          console.log(distribute)
          try {
            let res = await this.axios.post('/projectDistribute/', distribute)
          } catch (error) {
            console.log(error)
          }
        }
      }
      // 左边，删除数据
      if (direction == 'left') {
        for (let i = 0; i < movedKeys.length; i++) {
          try {
            let res = await this.axios.delete('/projectDistribute/' + movedKeys[i] + '/')
          } catch (error) {
            console.log(error)
          }
        }
      }
    }
  }
}
</script>

<style lang='less'>
.el-breadcrumb {
  margin-bottom: 20px;
}
.select {
  display: flex;
  .space {
    width: 180px;
  }
  .el-input {
    width: 400px;
  }
}

.data {
  display: flex;
  margin-top: 20px;
}
.el-transfer-panel {
  width: 400px;
}
</style>