<template>
  <div>
    <el-card>
      <!-- 1.面包屑 -->
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>
          <a>申报人管理</a>
        </el-breadcrumb-item>
        <el-breadcrumb-item>申报人管理</el-breadcrumb-item>
      </el-breadcrumb>
      <!-- 2.搜索框 -->
      <el-row class="row-search">
        <el-col>
          <el-input
            class="user-search"
            clearable
            placeholder="请输用户名"
            v-model="query"
          >
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
          <el-button type="success" plain>添加用户</el-button>
        </el-col>
      </el-row>
      <!-- 3.表格 -->
      <el-table :data="users" style="width: 100%">
        <el-table-column
          type="index"
          prop="date"
          label="序号"
          width="60"
        ></el-table-column>
        <el-table-column
          prop="username"
          label="姓名"
          width="120"
        ></el-table-column>
        <el-table-column
          prop="user_email"
          label="邮箱"
          width="120"
        ></el-table-column>
        <el-table-column
          prop="user_tel"
          label="电话"
          width="180"
        ></el-table-column>
        <el-table-column label="创建时间" width="120">
          <template slot-scope="users">{{
            users.row.create_time | fmtdate
          }}</template>
        </el-table-column>
        <el-table-column prop="is_active" label="用户状态" width="100">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.is_active"
              active-color="#13ce66"
              inactive-color="#ff4949"
            ></el-switch>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button
              size="mini"
              :plain="true"
              type="primary"
              icon="el-icon-edit"
              circle
            ></el-button>
            <el-button
              size="mini"
              @click="deleteUser(scope.row.user_id)"
              :plain="true"
              type="danger"
              icon="el-icon-delete"
              circle
            ></el-button>
            <el-button
              size="mini"
              :plain="true"
              type="success"
              icon="el-icon-check"
              circle
            ></el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 4.分页 -->
      <ul>
        <li v-for="(v, i) in users" :key="i">{{ v.is_active }}</li>
      </ul>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="400"
      ></el-pagination>
      <el-button @click.prevent="test()">test</el-button>
      <!-- 对话框 -->
      <!-- 5.添加用户对话框 -->
      <el-dialog title="增加用户" :visible.sync="addUserFormVisible">
        <el-form :model="addUserForm">
          <el-form-item label="用户名称" :label-width="formLabelWidth">
            <el-input v-model="addUserForm.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="用户密码" :label-width="formLabelWidth">
            <el-input
              v-model="addUserForm.password"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="addUserFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="addUserFormButton()"
            >确 定</el-button
          >
        </div>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: "",
      users: [],
      //分页
      currentPage: 1,
      //添加用户 对话框属性
      addUserFormVisible: false,
      formLabelWidth: "",
      addUserForm: { name: "", password: "" },
    };
  },
  created() {
    // this.getUsers();
  },
  methods: {
    //获取用户列表
    async getUsers() {
      const res = await this.axios.get("api/users/");
      if (res.status === 200) {
        this.users = res.data;
        console.log(res);
        //改is_active 为布尔型
        for (var i = 0; i < this.users.length; i++) {
          //test
          // console.log(this.users[i].is_active);
          if (this.users[i].is_active) {
            this.users[i].is_active = true;
          } else {
            this.users[i].is_active = false;
          }
        }
      } else {
        this.$message.warning("错误");
      }
    },
    //分页
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
    //测试
    async test() {
      var name = "10",
        price = 1000;
      const tdata = await this.axios.get(
        `/api/book/?name=${name}&price=${price}`
      );
      alert(tdata);
      console.log(tdata);
    },
    //添加用户
    showAddUserForm() {
      this.addUserFormVisible = true;
    },
    async addUserFormButton() {
      console.log(this.addUserForm.name, this.addUserForm.password);
      var data = {
        username: "0923",
        qq_open_id: "",
        password: "123456",
        user_email: "email",
        user_email_code: "",
        is_active: 0,
        user_sex: "1",
        user_qq: "33",
        user_tel: "1332233",
        user_xueli: "本科",
        user_hobby: "paly",
        user_introduce: "",
        create_time: 1324234234,
        update_time: 1147483647,
      };
      const res = await this.axios.post("api/users/", data);
      console.log(res);
      this.addUserFormVisible = false;
      this.getUsers();
    },
    //删除用户
    deleteUser(id) {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(async () => {
          const res = await this.axios.delete(`api/users/${id}`);
          console.log(res);
          this.$message({
            type: "success",
            message: "删除成功!",
          });
          this.getUsers();
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style>
.el-card {
  height: 100%;
}
.row-search {
  margin-top: 20px;
}
.user-search {
  width: 300px;
}
</style>