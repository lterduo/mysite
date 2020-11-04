<template>
  <div>
    <!-- 1.面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>申报书管理</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>申报书填写</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 搜索框 新增按钮-->
      <el-row class="row-search">
        <el-col class="el-col-user-add">
          <el-input class="user-search" clearable placeholder="请输申报书信息（用空格分隔），支持模糊搜索" v-model="query">
            <el-button slot="append" icon="el-icon-search" @click.prevent="queryUser()"></el-button>
          </el-input>
          <el-button class="bt-user-add" type="success" plain @click.prevent="showAddForm()">新增申报书</el-button>
        </el-col>
      </el-row>
      <!-- 申报书列表 -->
      <el-table :data="projectInfo" style="width: 100%">
        <el-table-column type="index" label="序号" width="60"></el-table-column>
        <el-table-column prop="name" label="名称" width="280"></el-table-column>
        <el-table-column label="创建时间" width="120">
          <template slot-scope="scope">{{
            scope.row.create_time | fmtdate
          }}</template>
        </el-table-column>
        <el-table-column prop="status" label="状态" width="90">
          <template slot-scope="scope">
            <div>{{statusName(scope.row.status)}}</div>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-edit" circle
              :disabled="scope.row.status==2?false:true" @click="showEditForm(scope.row.id)"></el-button>
            <!-- 只有状态为2（待修改）的才能点击修改按钮 -->
          </template>
        </el-table-column>
      </el-table>
      <!-- 申报书新增 -->
      <el-card v-show="addFormVisible">
        <el-row>
          <el-col :span="24">
            <div class="header-edit">新增申报书</div>
            <!-- 课题类别 -->
            <el-select v-model="projectCategory.id" style="width:420px;" filterable allow-create default-first-option
              placeholder="请选择课题类别">
              <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
              </el-option>
            </el-select>
          </el-col>
        </el-row>
      </el-card>
      <!-- 申报书修改 -->
      <el-card v-show="editFormVisible">
        <el-row>
          <el-col :span="24">
            <div class="header-edit">修改申报书</div>
            <!-- 课题类别 -->
            <el-select v-model="projectCategory.id" style="width:420px;" filterable allow-create default-first-option
              placeholder="请选择课题类别">
              <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
              </el-option>
            </el-select>
            <!-- <el-button class="bt-user-add" type="success" plain @click.prevent="showAddUserForm()">新增申报人</el-button> -->
          </el-col>
        </el-row>
      </el-card>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      userid: '',
      query: '',  //查询条件
      projectInfo: [],
      projectCategory: {},
      projectCategorys: {},
      projectStatus: [],
      status: '',
      addFormVisible: false,  //显示新增卡片      
      editFormVisible: false, // 显示编辑卡片
    }
  },
  created () {
    this.getProjectCategory()
    this.userid = localStorage.getItem("userid")
    this.getProjectInfo()
    this.getProjectStatus()
  },
  methods: {
    //获取课题类别
    async getProjectCategory () {
      const res = await this.axios.get(`/projectCategory/`)
      if (res.status === 200) {
        this.projectCategorys = res.data.results
        // console.log(this.projectCategorys)
      } else {
        this.$message.warning("错误")
      }
    },

    // 获取课题状态
    async getProjectStatus () {
      const res = await this.axios.get(`/projectStatus/`)
      if (res.status === 200) {
        this.projectStatus = res.data
        console.log(this.projectStatus)
      } else {
        this.$message.warning("错误")
      }
    },

    // 获取课题信息
    async getProjectInfo () {
      const res = await this.axios.get(`/projectInfo/?leader=${this.userid}`)
      if (res.status === 200) {
        this.projectInfo = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    // 查询课题信息
    async queryUser () {
      const res = await this.axios.get(`/projectInfo/?leader=${this.userid}&search=${this.query}`)
      if (res.status === 200) {
        this.projectInfo = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    // 显示新增申报书卡片
    showAddForm () {
      this.addFormVisible = true
      this.editFormVisible = false
    },

    // 显示编辑申报书卡片
    showEditForm (id) {
      this.editFormVisible = !this.editFormVisible
      this.addFormVisible = false
    },
    //获取状态名称
    // return好坑啊!!!!!!!!!!!!!!!!!!
    statusName (id) {
      name = ''
      this.projectStatus.forEach((s) => {
        if (s.s_id == id) {
          console.log(s.status)
          name = s.status
        }
      })
      return name
    },
    // 测试
    test () {
      this.editFormVisible = !this.editFormVisible
    },
  },
}
</script>

<style>
.el-card {
  margin-top: 15px;
}
.header-edit {
  font-size: 16px;
  text-align: center;
}
.el-col-user-add {
  display: flex;
}
.user-search {
  width: 420px;
  margin-right: 10px;
}
</style>