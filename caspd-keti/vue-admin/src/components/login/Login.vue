<template>
  <div class="bg-container">
    <div class="login-container">

      <!-- 标题 -->
      <div class="header">
        <h2>中国残疾人体育运动管理中心课题管理系统</h2>
      </div>
      <!-- 用户登陆和系统提示区 -->
      <div class="main">
        <el-row>
          <!-- 系统提示 -->
          <el-col :span="16" class="notice">
            <div class="guide">
              <h3>申报使用指南</h3>
              <h4>1. 新用户请点击注册按钮进行注册。</h4>
              <h4>2. 新注册的用户，其职称必须为副高或以上，且需将职称证明扫描后上传。</h4>
              <h4>3. 新用户注册后，需待管理员进行验证并激活后方可正常登陆使用。</h4>
              <h4>4. 申报流程：</h4>
              <div class="guide4">
                <p>(1)在使用指南底部文件列表中下载申报书模板</p>
                <p>(2)登录后，点击“申报书管理/申报书填写”菜单，点击“新增申报书”按钮，将课题相关信息录入到对应的表单中。</p>
                <p>(3)录入过程中可以点击“保存”按钮临时保存，方便下次继续录入。再次录入时，点击申报书列表中“操作”项的编辑按钮，即可继续录入。</p>
                <p>(4)信息录入完毕后，可以点击“生成申报书”按钮，自动生成申报书。
                </p>
                <p>(5)将申报书签字盖章后扫描，在申报书列表的“操作”项中点击编辑按钮，将扫描件和《前期研究成果》、《在研课题证明》分别上传到服务器，
                  点击“提交审核”等待审核。
                </p>
              </div>
            </div>
            <!-- 指南文件列表 -->
            <el-table class="guideFileTable" :data="guideFileList" border style="width:401px;">
              <el-table-column prop="name" label="指南文件" width="300"></el-table-column>
              <el-table-column label="操作" width="100">
                <template slot-scope="scope">
                  <el-button size="mini" :plain="true" type="primary" icon="el-icon-download" circle
                    @click="downloadFile(scope.row)"></el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-col>
          <!-- 用户登陆 -->
          <el-col :span="8" class="login">
            <el-card>
              <el-form class="login-form" :model="loginForm">
                <el-form-item>
                  <el-input v-model="loginForm.userid" placeholder="账号"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-input v-model="loginForm.password" placeholder="密码" show-password></el-input>
                </el-form-item>
                <div>
                  <!-- <Verify :type="3" @success="success"></Verify> -->
                  <Verify :type="3" @success="success" :barSize="{width:'300px',height:'40px'}" :showButton="false">
                  </Verify>
                </div>
              </el-form>
              <div class="button-login">
                <el-button type="primary" @click.prevent="handleReg()">注册</el-button>
                <el-button type="primary" @click.prevent="handleLogin()">登录</el-button>
              </div>
            </el-card>
          </el-col>
        </el-row>
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
          <el-input v-model="addUserForm.userid" autocomplete="off" @blur="useridVerify()" id="id-userid"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.password" show-password autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="passwordConfirm" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.passwordConfirm" show-password autocomplete="off" @blur="confirmPass()"
            id="id-pass-confirm">
          </el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="username" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="gender" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.gender" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="民族" prop="national" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.national" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="出生年月" prop="birth" :label-width="formLabelWidth">

          <el-date-picker v-model="addUserForm.birth" type="date" placeholder="选择日期" format="yyyy年MM月dd日"
            value-format="yyyy-MM-dd">
          </el-date-picker>
          {{addUserForm.birth}}
        </el-form-item>
        <el-form-item label="单位" prop="organization" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.organization" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="职称级别" prop="title_level" :label-width="formLabelWidth">
          <el-select v-model="addUserForm.title_level" placeholder="请选择职称级别" style="width:100%;">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="专业职称" prop="duty" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.duty" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="行政职务" prop="title" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.title" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="研究专长" prop="major" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.major" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最后学历" prop="education" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.education" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最后学位" prop="degree" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.degree" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所在省（自治区、直辖市）" prop="province" label-width="30%">
          <el-input v-model="addUserForm.province" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="通讯地址" prop="addr" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.addr" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="联系电话" prop="tel" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.tel" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="E-mail" prop="email" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮政编码" prop="zipcode" :label-width="formLabelWidth">
          <el-input v-model="addUserForm.zipcode" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>

      <!-- 处理职称文件 -->
      <div class="div-file">
        <!-- 上传附件 -->
        <div class="div-upload">
          <input type="file" value="" class="input-upload" @change="uploadFileEdit">
          <el-button type="primary" size="small" class="button-upload">上传职称证明
            <i class="el-icon-upload el-icon--right"></i>
          </el-button>
        </div>
        <!-- 文件列表 -->
        <el-table :data="fileList" border style="width:551px;" :header-cell-style="{background:'#fafafa'}">
          <el-table-column prop="name" label="文件名" width="300"></el-table-column>
          <el-table-column prop="create_time" label="创建时间" width="150">
            <template slot-scope="scope">
              {{scope.row.create_time | fmtdate}}
            </template>
          </el-table-column>
          <el-table-column label="操作" width="100">
            <template slot-scope="scope">
              <el-button size="mini" :plain="true" type="primary" icon="el-icon-download" circle
                @click="downloadFile(scope.row)"></el-button>
              <el-button size="mini" :plain="true" type="danger" icon="el-icon-delete" circle
                @click="deleteFile(scope.row)">
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <div slot="footer" class="dialog-footer">
        <el-button @click="addUserFormVisible=false">取 消</el-button>
        <el-button type="primary" @click="addUserFormButton()">确 定</el-button>
      </div>

    </el-dialog>
  </div>
</template>

<script>
import Verify from 'vue2-verify'
import fileDownload from 'js-file-download'

export default {
  components: { Verify },

  data () {
    return {
      loginForm: { userid: "", password: "" },
      data: {},
      verifyCode: false,
      // 指南文件
      guideFileList: [
        { name: '申报书模板.doc', path: './uploadfiles/指南文件/申报书模板.doc' },
        { name: '保密及权属协议书.docx', path: './uploadfiles/指南文件/保密及权属协议书.docx' }
      ],
      // 用户注册
      addUserFormVisible: false,
      formLabelWidth: '',
      addUserForm: {},
      // 上传的职称文件
      fileList: [],
      // 添加用户对话框校验规则
      addUserFormRules: {
        userid: [{ required: true, message: '请输入账号', trigger: 'blur' }, { min: 2, max: 32, message: '长度在 2 到 32 个字符', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' },],
        passwordConfirm: [{ required: true, message: '请输入密码', trigger: 'blur' }],
        username: [{ required: true, message: '请输入姓名', trigger: 'blur' },],
        gender: [{ required: true, message: '请输入性别', trigger: 'blur' },],
        national: [{ required: true, message: '请输入民族', trigger: 'blur' },],
        birth: [{ required: true, message: '请输入出生年月', trigger: 'blur' },],
        organization: [{ required: true, message: '请输入单位', trigger: 'blur' },],
        title_level: [{ required: true, message: '请选择职称级别', trigger: 'blur' },],
        title: [{ required: true, message: '请输入专业职称', trigger: 'blur' },],
        duty: [{ required: true, message: '请输入行政职务', trigger: 'blur' },],
        major: [{ required: true, message: '请输入研究专长', trigger: 'blur' },],
        education: [{ required: true, message: '请输入最后学历', trigger: 'blur' },],
        degree: [{ required: true, message: '请输入最后学位', trigger: 'blur' },],
        province: [{ required: true, message: '请输入所在省（自治区、直辖市）', trigger: 'blur' },],
        addr: [{ required: true, message: '请输入通讯地址', trigger: 'blur' },],
        tel: [{ required: true, message: '请输入联系电话', trigger: 'blur' },],
        email: [{ required: true, message: '请输入E-mail', trigger: 'blur' },],
        zipcode: [{ required: true, message: '请输入邮政编码', trigger: 'blur' },],
      },

      // 职称级别
      options: [{
        value: '副高',
        label: '副高'
      }, {
        value: '正高',
        label: '正高'
      }],
    };
  },


  methods: {
    // 验证码
    success (e) {
      //成功后的返回
      this.verifyCode = true
    },

    // 登陆
    async handleLogin () {
      if (!this.verifyCode) {
        return this.$message.error('请完成验证！')
      }
      // 判断账号密码不能为空
      if (!this.loginForm.userid || !this.loginForm.password) {
        return this.$message.error("账号和密码不能为空！")
        // return this.$message.warning("账号或密码不能为空！") 
      }

      const res = await this.axios.post("/login/", this.loginForm)
      this.data = res.data
      if (this.data.code === 1000) {
        // 是否激活
        if (this.data.is_active) {
          //获取菜单列表
          let url = '/role/?role_id=' + this.data.role_id
          let resMenu = await this.axios.get('/role/?role_id=' + this.data.role_id)
          if (resMenu.status == 200) {
            resMenu = resMenu.data.results[0]
            localStorage.setItem("menus", JSON.stringify(resMenu.menus))
          } else {
            this.$message.error('获取权限失败！')
          }

          this.$message.success(this.data.msg)
          //保存token
          localStorage.setItem("userid", this.data.userid)
          localStorage.setItem("username", this.data.username)
          localStorage.setItem("token", this.data.token)
          this.$router.push("home")
        } else {
          this.$message.warning('账号未激活！')
        }
      } else {
        this.$message.warning(this.data.msg)
      }
    },

    // 注册按钮
    handleReg () {
      this.addUserFormVisible = true
    },

    // 验证userid是否被占用
    async useridVerify () {
      const res = await this.axios.get('/user/?userid=' + this.addUserForm.userid)
      if (res.data.results.length === 1) {
        this.$message.error('账号已被注册，请更换账号名称！')
        document.getElementById('id-userid').focus()
      }
    },

    // 新增注册账户
    async addUserFormButton () {
      this.addUserForm.role_id = 2
      const res = await this.axios.post("/user/", this.addUserForm)

      if (res.status === 201) {
        this.$message.success('注册成功，等待管理员激活。')
      }
      this.addUserFormVisible = false
    },

    // 验证密码是否一致
    confirmPass () {

      if (this.addUserForm.password != this.addUserForm.passwordConfirm) {

        this.$message.warning('密码不一致，请重新填写！')
        this.addUserForm.passwordConfirm = ''
        setTimeout(() => {
          document.getElementById('id-pass-confirm').focus()
        }, 500);
      }
    },


    // 获取附件列表
    async getFileList (pid) {
      const res = await this.axios.get(`/fileList/?pid=${pid}`)
      if (res.status === 200) {
        this.fileList = res.data.results
      } else {
        this.$message.warning("获取文件列表错误")
      }
    },

    //上传文件
    uploadFileEdit (e) {
      let formData = new FormData();
      let pid = '职称证明/' + this.addUserForm.userid
      let data = JSON.stringify({
        pid
      })
      formData.append('file', e.target.files[0]);
      formData.append('data', data);   // 上传文件的同时， 也可以上传其他数据
      let url = `/uploadFile/`;
      let config = {
        headers: { 'Content-Type': 'multipart/form-data' }
      };
      this.axios.post(url, formData, config).then((response) => {
        // console.log(response.data)
        this.getFileList(pid)
        // console.log('fileList:  ', this.fileList)
      })
    },

    // 删除文件
    async deleteFile (item) {
      let res = await this.axios.delete('/fileList/' + item.id + '/')
      if (res.status === 204) {
        this.getFileList(item.pid)
      }
      let data = { path: item.path }
      let resDelete = await this.axios.post('/deleteFile/', data)
    },

    // 下载文件
    downloadFile (item) {
      let url = `/downloadFile/?path=${item.path}&name=${item.name}`
      let params = {
        path: item.path,
        name: item.name
      }
      this.axios.post(url, params, { responseType: 'arraybuffer' }).then(res => {
        fileDownload(res.data, item.name)
      })
    },

  },
};
</script>

<style  lang='less'>
h2 {
  padding-bottom: 10px;
  border-bottom: 2px solid black;
}
h3 {
  padding-left: 20px;
  padding-bottom: 10px;
  margin-bottom: 30px;
  border-bottom: 1px solid black;
  font-size: 22px;
}
.bg-container {
  background-image: url("../../assets/image/login-bg1.png");

  .login-container {
    width: 1200px;
    height: 100%;
    margin: 0 auto;

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
      height: 740px;
      .notice {
        padding: 20px;
        .guide {
          .guide4 {
            margin-top: -10px;
            p {
              margin: 0;
              line-height: 30px;
            }
          }
        }
        .guideFileTable {
          margin: 30px 0 0 0px;
          .el-table th,
          .el-table tr,
          .el-table td {
            background-color: transparent;
          }
        }
      }
      .login {
        margin-top: 150px;
        padding-left: 40px;
        .el-card {
          margin-right: 20px;
          .button-login {
            display: flex;
            justify-content: end;
            margin-top: 60px;
          }
        }
      }
    }

    .footer {
      font-size: 13px;
      text-align: center;
      padding-bottom: 10px;
    }
  }
  .div-file {
    margin-top: 15px;
    .div-upload {
      height: 47px;
      .input-upload {
        width: 73px;
        height: 33px;
        position: absolute;
        z-index: 1;
        opacity: 0;
      }
      .button-upload {
        position: absolute;
      }
      .button-upload:hover {
        cursor: pointer;
      }
    }
  }
}

.el-table th,
.el-table tr,
.el-table td {
  background-color: transparent;
}
.el-table--striped .el-table__body tr.el-table__row--striped td {
  background-color: #fff;
  background-color: rgba(148, 144, 144, 0.3);
}
.el-table th,
.el-table tr {
  background-color: transparent;
}

.el-dialog {
  z-index: 10;
}
</style>