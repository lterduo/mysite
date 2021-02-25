<template>
  <div>
    <!-- 1.面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>专家管理</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>专家管理</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 2.搜索框 -->
      <el-row class="row-search">
        <el-col class="el-col-user-add">
          <el-input class="user-search" clearable placeholder="请输用户信息（用空格分隔），支持模糊搜索" v-model="query">
            <el-button slot="append" icon="el-icon-search" @click.prevent="queryUser()"></el-button>
          </el-input>
          <el-button class="bt-user-add" type="success" plain @click.prevent="showAddUserForm()">新增专家</el-button>
        </el-col>
      </el-row>
      <!-- 3.表格 -->
      <el-table :data="users" style="width: 100%">
        <el-table-column label="详情" type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="地址：">
                <span>{{ props.row.addr }}</span>
              </el-form-item>
              <el-form-item label="电话：">
                <span>{{ props.row.tel }}</span>
              </el-form-item>
              <el-form-item label="开户行：">
                <span>{{ props.row.bank.bank}}</span>
                <span> </span>
                <span>{{props.row.bank.account}}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column type="index" label="序号" width="60"></el-table-column>
        <el-table-column prop="userid" label="id" width="100"></el-table-column>
        <el-table-column prop="username" label="姓名" width="80"></el-table-column>
        <el-table-column prop="organization" label="单位" width="120"></el-table-column>
        <el-table-column prop="major" label="研究方向" width="180"></el-table-column>
        <el-table-column label="创建时间" width="120">
          <template slot-scope="scope">
            {{scope.row.create_time | fmtdate}}</template>
        </el-table-column>
        <el-table-column prop="is_active" label="用户状态" width="90">
          <template slot-scope="scope">
            <el-switch v-model="scope.row.is_active" active-color="#13ce66" inactive-color="#ff4949"
              @change="userIsActive(scope.row)"></el-switch>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-edit" circle
              @click="showEditUserForm(scope.row.userid)"></el-button>
            <el-button size="mini" :plain="true" type="danger" icon="el-icon-delete" circle
              @click="deleteUser(scope.row.userid)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 4.分页 -->
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage"
        :page-sizes="[10, 20, 50]" :page-size="page_size" layout="total, sizes, prev, pager, next, jumper"
        :total="total"></el-pagination>
      <!-- 对话框 -->
      <!-- 5.添加用户对话框 -->
      <el-dialog title="新增专家" :visible.sync="addUserFormVisible">
        <el-form label-position="left" label-width="80px" :model="addUserForm" :rules="addUserFormRules">
          <el-form-item label="用户id" prop="userid" :label-width="formLabelWidth">
            <el-input v-model="addUserForm.userid" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="用户密码" prop="password">
            <el-input v-model="addUserForm.password" show-password autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="用户姓名" prop="username" :label-width="formLabelWidth">
            <el-input v-model="addUserForm.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="研究方向" :label-width="formLabelWidth">
            <el-input v-model="addUserForm.major" autocomplete="off"></el-input>
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
          <el-form-item label="开户银行" :label-width="formLabelWidth">
            <el-input v-model="addUserForm.bank.bank" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="银行账号" :label-width="formLabelWidth">
            <el-input v-model="addUserForm.bank.account" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="是否激活" :label-width="formLabelWidth">
            <el-switch v-model="addUserForm.is_active" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="addUserFormVisible=false">取 消</el-button>
          <el-button type="primary" @click="addUserFormButton()">确 定</el-button>
        </div>
      </el-dialog>
      <!-- 修改用户对话框 -->
      <el-dialog title="修改专家信息" :visible.sync="editUserFormVisible">
        <el-form label-position="left" label-width="80px" :model="editUserForm" :rules="addUserFormRules">
          <el-form-item label="用户id" prop="userid" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.userid" autocomplete="off" disabled></el-input>
          </el-form-item>
          <el-form-item label="用户密码" prop="password" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.password" show-password autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="用户姓名" prop="username" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="研究方向" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.major" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="单位" prop="organization" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.organization" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="电话" prop="tel" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.tel" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.email" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="地址" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.addr" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开户银行" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.bank.bank" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="银行账号" :label-width="formLabelWidth">
            <el-input v-model="editUserForm.bank.account" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="是否激活" :label-width="formLabelWidth">
            <el-switch v-model="editUserForm.is_active" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="editUserFormVisible=false">取 消</el-button>
          <el-button type="primary" @click="editUserFormButton()">确 定</el-button>
        </div>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      query: "",  //查询信息
      users: [],
      //分页
      currentPage: 1,
      page_size: 10,
      total: 0,
      //添加用户 对话框属性
      addUserFormVisible: false,
      // 修改用户 对话框属性
      editUserFormVisible: false,
      formLabelWidth: "",
      addUserForm: {
        role_id: 3,
        bank: { bank: '', account: '' },
      },
      // 添加用户对话框校验规则
      addUserFormRules: {
        userid: [
          { required: true, message: '请输入id', trigger: 'blur' },
          { min: 2, max: 32, message: '长度在 2 到 32 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
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
      editUserForm: {
        bank: { bank: '', account: '' }
      },
    }
  },
  created () {
    this.getUsers(1, 10)
  },
  methods: {
    //获取用户列表
    async getUsers (page, page_size) {
      const res = await this.axios.get(
        `/user/?role_id=3&page=${page}&page_size=${page_size}`
      )
      if (res.status === 200) {
        this.users = res.data.results
        this.total = res.data.count
        console.log(res)
      } else {
        this.$message.warning("错误")
      }
    },
    //分页
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`)
      this.page_size = val
      this.getUsers(this.currentPage, this.page_size)
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
      this.currentPage = val
      this.getUsers(this.currentPage, this.page_size)
    },

    // 查询用户
    async queryUser () {
      const res = await this.axios.get(
        `/user/?role_id=3&page=${this.currentPage}&page_size=${this.page_size}&search=${this.query}`
      )
      if (res.status === 200) {
        this.users = res.data.results
        this.total = res.data.count
        console.log(res)
      } else {
        this.$message.warning("错误")
      }
    },

    //添加用户
    showAddUserForm () {
      this.addUserFormVisible = true
    },

    async addUserFormButton () {
      const res = await this.axios.post("/user/", this.addUserForm)
      console.log(this.addUserForm)
      this.addUserFormVisible = false
      this.getUsers(this.currentPage, this.page_size)
    },

    // 编辑用户
    async showEditUserForm (id) {
      const res = await this.axios.get('/user/' + id)
      if (res.status !== 200) {
        return this.$message.error('查询用户信息失败！')
      }
      this.editUserForm = res.data
      this.editUserFormVisible = true
    },

    editUserFormButton () {
      this.$confirm("此操作将修改用户信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(async () => {
          var url = '/user/' + this.editUserForm.userid + '/'
          console.log(url)
          const res = await this.axios.put(url, this.editUserForm)
          if (res.status !== 200) {
            return this.$message.error('更新用户状态失败')
          }
          this.$message({
            type: "success",
            message: "修改成功!",
          })
          this.editUserFormVisible = false
          this.getUsers(this.currentPage, this.page_size)
        })
        .catch(() => {
          this.$message.error('更新用户状态失败')
        })
    },

    //切换用户是否激活状态
    async userIsActive (user) {
      var url = '/user/' + user.userid + '/'
      var data = { userid: user.userid, is_active: user.is_active }
      const res = await this.axios.put(url, user)
      // const res = await this.axios.get(url)
      console.log(res)
      if (res.status !== 200) {
        user.is_active = !user.is_active
        return this.$message.error('更新用户状态失败')
      }
      this.$message.success('更新用户状态成功！')
    },

    //删除用户
    deleteUser (id) {
      this.$confirm("此操作将永久删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(async () => {
          const res = await this.axios.delete(`/user/${id}`)
          console.log(res)
          this.$message({
            type: "success",
            message: "删除成功!",
          })
          this.getUsers(this.currentPage, this.page_size)
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          })
        })
    },
  },
} 
</script>

<style lang='less'>
.el-card {
  height: 100%;
  margin-top: 15px;
}
.row-search {
  margin-top: 20px;
}
.user-search {
  width: 420px;
}
.el-pagination {
  margin-top: 15px;
}
.el-col-user-add {
  display: flex;
}
.bt-user-add {
  margin-left: 10px;
}

.demo-table-expand {
  font-size: 0;
  label {
    width: 90px;
    color: #99a9bf;
  }
  .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
}
</style>