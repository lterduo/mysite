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
              <el-input v-model="loginForm.password" placeholder="用户密码" show-password></el-input>
            </el-form-item>
            <div>
              <Verify :type="3" @success="success"></Verify>
            </div>
          </el-form>
          <div class="button-login">
            <el-button type="primary" @click.prevent="handleLogin()">登录</el-button>
            <el-button type="primary" @click.prevent="handleReg()">注册</el-button>
          </div>
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
    <!-- 注册对话框 -->
    <el-dialog title="用户注册" :visible.sync="addUserFormVisible">
      <el-form label-position="left" label-width="80px" :model="addUserForm" ref="ruleForm" :rules="addUserFormRules"
        class="demo-ruleForm">
        <el-form-item label="账号" prop="userid">
          <el-input v-model="addUserForm.userid" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.password" show-password autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="passwordConfirm" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.passwordConfirm" show-password autocomplete="off" @blur="confirmPass"
            id="id-pass-confirm">
          </el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="username" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="单位" prop="organization" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.organization" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="tel" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.tel" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="地址" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.addr" autocomplete="off"></el-input>
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addUserFormVisible=false">取 消</el-button>
        <el-button type="primary" @click="addUserFormButton()">确 定</el-button>
      </div>
      <el-button @click="test()">focus</el-button>
    </el-dialog>
  </div>
</template>

<script>
import Verify from 'vue2-verify'

export default {
  components: { Verify },

  data () {
    return {
      loginForm: { userid: "", password: "" },
      data: {},
      verifyCode: false,
      // 用户注册
      addUserFormVisible: false,
      formLabelWidth: '',
      addUserForm: {},
      // 添加用户对话框校验规则
      addUserFormRules: {
        userid: [
          { required: true, message: '请输入id', trigger: 'blur' },
          { min: 2, max: 32, message: '长度在 2 到 32 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
        ],
        passwordConfirm: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        username: [
          { required: true, message: '请输入姓名', trigger: 'blur' },
        ],
        organization: [
          { required: true, message: '请输入单位', trigger: 'blur' },
        ],
        tel: [
          { required: true, message: '请输入电话', trigger: 'blur' },
        ]
      },
    };
  },

  methods: {
    success (e) {
      //成功后的返回
      this.verifyCode = true
    },


    async handleLogin () {
      // if (!this.verifyCode) {
      //   return this.$message.error('验证码错误')
      // }
      // // 判断账号密码不能为空
      // if (!this.loginForm.userid || !this.loginForm.password) {
      //   return this.$message.error("账号和密码不能为空！")
      //   // return this.$message.warning("账号或密码不能为空！") 
      // }
      // //$message是element ui 的对象
      // // this.$message.succes('开始登录')//'' 普通 ,'warning' ,  'error'
      // //请求数据
      // //async/await 写法
      // const res = await this.axios.post("/login/", this.loginForm)
      // this.data = res.data
      // console.log(res)
      // if (this.data.code === 1000) {
      //   this.$message.success(this.data.msg)
      //   //保存token
      //   localStorage.setItem("userid", this.data.userid)
      //   localStorage.setItem("token", this.data.token)
      //   this.$router.push("home")
      // } else {
      //   this.$message.warning(this.data.msg)
      // }
      console.log('login')
      this.$router.push("home")

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
    handleReg () {
      this.addUserFormVisible = true
    },
    async addUserFormButton () {
      const res = await this.axios.post("/user/", this.addUserForm)
      console.log(res)
      this.addUserFormVisible = false
    },
    confirmPass () {
      console.log(this.addUserForm)
      if (this.addUserForm.password != this.addUserForm.passwordConfirm) {
        console.log(this.addUserForm.passwordConfirm)
        this.$message.warning('密码不一致，请重新填写！')
        this.addUserForm.passwordConfirm = ''
        document.getElementById('id-pass-confirm').focus()
      }
    },
    test () {
      document.getElementById('id-pass-confirm').focus()
    }
  },
};
</script>

<style  lang='less'>
.bg-container {
  background: #eee;
  background-image: url("../../assets/image/login-bg1.png");
}
h3 {
  padding-left: 20px;
  padding-bottom: 20px;
  margin-bottom: 30px;
  border-bottom: 1px solid black;
}
.login-container {
  width: 1200px;
  height: 100%;
  margin: 0 auto;
}
.header {
  width: 100%;
  height: 130px;
  // background: #fff;
  font-size: 24px;
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  // opacity: 0.3;
}
.main {
  margin: 5px 0;
  width: 100%;
  display: flex;
  justify-content: center;
}
.login {
  flex: 1;
  // background: #fff;
  padding: 20px;
  // 验证码按钮
  .verify-btn {
    visibility: hidden;
  }
  .button-login {
    margin-top: 20px;
  }
}
.notice {
  flex: 1;
  padding: 20px;
  // background: #fff;
}
.download {
  box-sizing: border-box;
  padding: 20px;
  width: 100%;
  height: 380px;
  // background: #fff;
}
.footer {
  font-size: 13px;
  text-align: center;
}
</style>