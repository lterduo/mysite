<template>
  <div class="login_container">
    <el-form class="login-form" label-position="top" label-width="80px" :model="formLabelAlign">
      <h2>用户登录</h2>
      <el-form-item label="用户名称">
        <el-input v-model="formLabelAlign.username"></el-input>
      </el-form-item>
      <el-form-item label="用户密码">
        <el-input v-model="formLabelAlign.password"></el-input>
      </el-form-item>
      <el-button class="login-btn" type="primary" @click.prevent="handleLogin()">登录</el-button>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formLabelAlign: { username: "", password: "" },
      data: {},
    };
  },
  methods: {
    async handleLogin() {
      //$message是element ui 的对象
      // this.$message.succes('开始登录')//'' 普通 ,'warning' ,  'error'
      //请求数据
      //async/await 写法
      const res = await this.axios.post("api/login/", this.formLabelAlign)
        this.data = res.data;
        console.log(res)
        if (this.data.code === 100) {
          this.$message.success(this.data.msg);
          //保存token
          localStorage.setItem('token', this.data.token)
          this.$router.push("home");
        } else {
          this.$message.warning(this.data.msg);
        }
      //.then写法
      // this.axios.post("api/login/", this.formLabelAlign).then((res) => {
      //   this.data = res.data;
      //   if (this.data.code === 100) {
      //     this.$message.success(this.data.msg);
      //     this.$router.push("home");
      //   } else {
      //     this.$message.warning(this.data.msg);
      //   }
      // });

    },
  },
};
</script>

<style>
.login_container {
  background-color: #2b4b6b;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login_container .login-form {
  background-color: #fff;
  width: 400px;
  border-radius: 5px;
  padding: 20px;
}
.login_container .login-btn {
  width: 100%;
  margin-top: 20px;
}
</style>