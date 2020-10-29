<template>

  <div>
    <el-button @click="test()"></el-button>

    <el-form :model="ruleForm" :rules="rules" label-width="100px" class="demo-ruleForm">
      <el-form-item label="活动名称" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
    </el-form>

  </div>

</template>

<script>
export default {
  data () {
    return {
      ruleForm: {
        name: '',
      },
      addUserForm: {},
      rules: {
        name: [
          { required: true, message: '请输入活动名称', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
      }
    };
  },
  methods: {
    async test () {
      var data = JSON.stringify({ userid: 'lisi10', email: 'test@qq.com' })
      const res = await this.axios.put('/user/lisi10/', data)
      if (res.status !== 200) {
        return this.$message.error('查询用户信息失败！')
      }
    },
  }
};
</script>

<style>
</style>