<template>
  <div>
    <!-- 1.面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>客户信息维护</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>客户信息录入</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 客户照片 -->
      <img :src="imgName" class="image">
      <el-card title="新增申报人">
        <el-form label-position="left" label-width="80px" :model="addUserForm" :rules="addUserFormRules"
          class="demo-ruleForm">
          <el-form-item label="姓名" prop="username">
            <el-input v-model="addUserForm.username"></el-input>
          </el-form-item>
          <el-form-item label="单位" prop="organization">
            <el-input v-model="addUserForm.organization"></el-input>
          </el-form-item>
          <el-form-item label="电话" prop="tel">
            <el-input v-model="addUserForm.tel"></el-input>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="addUserForm.email"></el-input>
          </el-form-item>
          <el-form-item label="地址">
            <el-input v-model="addUserForm.addr"></el-input>
          </el-form-item>
        </el-form>

        <el-button type="primary" @click="addUserButton()">确 定</el-button>

      </el-card>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      imgName: '',

      addUserForm: {},
      // 添加用户对话框校验规则
      addUserFormRules: {
        username: [
          { required: true, message: '请输入姓名', trigger: 'blur' },
        ],
      },
    }
  },
  mounted () {
    console.log(this.$route.params)
    this.imgName = this.$route.params.filename
  },
  methods: {
    //添加用户
    async addUserButton () {
      const res = await this.axios.post("/user/", this.addUserForm)
      console.log(res)
    },
  },
} 
</script>

<style lang="less" scoped>
.el-card {
  height: 100%;
  margin-top: 15px;
}
</style>