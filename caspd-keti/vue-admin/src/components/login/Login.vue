<template>
  <div class="bg-container">
    <div class="login-container">
      <!-- 标题 -->
      <div class="header">
        <h2>中国残疾人体育运动管理中心课题申报系统</h2>
      </div>
      <!-- 用户登陆和系统提示区 -->
      <div class="main">
        <!-- 用户登陆 -->
        <div class="login">
          <h3>用户登陆</h3>
          <el-form class="login-form" :model="loginForm">
            <el-form-item>
              <el-input v-model="loginForm.userid" placeholder="用户id"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input v-model="loginForm.password" placeholder="用户密码"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input v-model="loginForm.password" placeholder="验证码"></el-input>

            </el-form-item>
            <el-form-item class="login-btn">
              <el-button type="primary" @click.prevent="handleLogin()">登录</el-button>
            </el-form-item>
          </el-form>
        </div>
        <!-- 系统提示 -->
        <div class="notice">
          <h3>系统提示</h3>
        </div>
      </div>
      <!-- 工作指南和下载 -->
      <div class="download">
        <h3>工作指南</h3>
      </div>
      <div class="footer">
        <p>中国残疾人体育运动管理中心</p>
        <p>
          地址：北京市顺义区后沙峪镇天北路321号 电话:010-80471809
          传真：010-80471809
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: { userid: "", password: "" },
      data: {},
    };
  },
  methods: {
    async handleLogin () {
      // 判断账号密码不能为空
      if (!this.loginForm.userid || !this.loginForm.password) {
        return this.$message.error("账号和密码不能为空！")
        // return this.$message.warning("账号或密码不能为空！") 
      }
      //$message是element ui 的对象
      // this.$message.succes('开始登录')//'' 普通 ,'warning' ,  'error'
      //请求数据
      //async/await 写法
      const res = await this.axios.post("/login/", this.loginForm)
      this.data = res.data
      console.log(res)
      if (this.data.code === 1000) {
        this.$message.success(this.data.msg)
        //保存token
        localStorage.setItem("userid", this.data.userid)
        localStorage.setItem("token", this.data.token)
        this.$router.push("home")
      } else {
        this.$message.warning(this.data.msg)
      }
      // .then写法
      // this.axios.post("api/login/", this.loginForm).then((res) => {
      //   this.data = res.data
      //   if (this.data.code === 100) {
      //     this.$message.success(this.data.msg)
      //     this.$router.push("home")
      //   } else {
      //     this.$message.warning(this.data.msg)
      //   }
      // });
    },
  },
};
</script>

<style scoped>
.bg-container {
  background: #eee;
  background-image: url("../../assets/image/login-bg1.png");
}
h3 {
  padding-left: 20px;
  padding-bottom: 20px;
  margin-bottom: 30px;
  border-bottom: 1px solid #bbb;
}
.login-container {
  width: 1200px;
  height: 100%;
  margin: 0 auto;
}
.header {
  width: 100%;
  height: 130px;
  background: #fff;
  line-height: 130px;
  font-size: 24px;
  text-align: center;
}
.main {
  margin: 5px 0;
  width: 100%;
  display: flex;
  justify-content: center;
}
.login {
  flex: 1;
  background: #fff;
  padding: 20px;
}
.notice {
  flex: 1;
  padding: 20px;
  background: #fff;
}
.download {
  box-sizing: border-box;
  padding: 20px;
  width: 100%;
  height: 380px;
  background: #fff;
}
.footer {
  font-size: 13px;
  text-align: center;
}
</style>