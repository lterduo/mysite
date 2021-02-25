<template>
  <div>
    <!-- 1.面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>课题类别管理</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>课题类别管理</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 2.搜索框 -->
      <el-row class="row-search">
        <el-col class="el-col-user-add">
          <el-input class="user-search" clearable placeholder="请输课题类别信息（用空格分隔），支持模糊搜索" v-model="query">
            <el-button slot="append" icon="el-icon-search" @click.prevent="queryUser()"></el-button>
          </el-input>
          <el-button class="bt-user-add" type="success" plain @click.prevent="showAddUserForm()">新增课题类别</el-button>
        </el-col>
      </el-row>
      <h3>注意：只能存在一个激活的课题类别！</h3>
      <!-- 3.表格 -->
      <el-table :data="users" style="width: 100%">
        <el-table-column type="index" label="序号" width="60"></el-table-column>
        <el-table-column prop="name" label="名称" width="280"></el-table-column>
        <el-table-column prop="desc" label="描述" width="520"></el-table-column>
        <el-table-column label="编辑课题类别方向" width="140">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-tickets" circle
              @click="showEditSonForm(scope.row)"></el-button>
          </template>
        </el-table-column>
        <el-table-column prop="is_active" label="状态" width="60">
          <template slot-scope="scope">
            <el-switch v-model="scope.row.is_active" active-color="#13ce66" inactive-color="#ff4949"
              @change="categoryIsActive(scope.row)"></el-switch>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-edit" circle
              @click="showEditUserForm(scope.row.id)"></el-button>
            <el-button size="mini" :plain="true" type="danger" icon="el-icon-delete" circle
              @click="deleteUser(scope.row)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 4.分页 -->
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage"
        :page-sizes="[10, 20, 50]" :page-size="page_size" layout="total, sizes, prev, pager, next, jumper"
        :total="total"></el-pagination>
      <!-- 对话框 -->
      <!-- 5.添加对话框 -->
      <el-dialog title="新增课题类别" :visible.sync="addUserFormVisible">
        <el-form label-position="left" label-width="80px" :model="addUserForm" :rules="addUserFormRules">
          <el-form-item label="名称" prop="name">
            <el-input v-model="addUserForm.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="描述" prop="desc">
            <el-input v-model="addUserForm.desc" type="textarea" :rows="2" placeholder="请输入描述内容"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="addUserFormVisible=false">取 消</el-button>
          <el-button type="primary" @click="addUserFormButton()">确 定</el-button>
        </div>
      </el-dialog>
      <!-- 修改对话框 -->
      <el-dialog title="修改课题类别信息" :visible.sync="editUserFormVisible">
        <el-form label-position="left" label-width="80px" :model="editUserForm" :rules="addUserFormRules">
          <el-form-item label="名称" prop="name">
            <el-input v-model="editUserForm.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="描述" prop="desc">
            <el-input v-model="editUserForm.desc" type="textarea" :rows="2" placeholder="请输入描述内容"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="editUserFormVisible=false">取 消</el-button>
          <el-button type="primary" @click="editUserFormButton()">确 定</el-button>
        </div>
      </el-dialog>
      <!-- 编辑子类对话框 -->
      <el-dialog :title="'父类名称： '+ father_name" :visible.sync="editSonFormVisible">
        <el-form :inline="true" class="demo-form-inline" v-for="item in sonFormArr" :key="item.index">
          <el-form-item label="名称">
            <el-input v-model="item.name"></el-input>
          </el-form-item>
          <el-form-item label="描述">
            <el-input v-model="item.desc"></el-input>
          </el-form-item>
          <el-button type="primary" @click="EditSonDirection(item.index)">编辑方向</el-button>
          <el-button type="primary" @click="DeleteSon(item.index)">删除</el-button>
        </el-form>
        <el-button type="primary" @click="AddSonForm">增加</el-button>

        <div slot="footer" class="dialog-footer">
          <el-button @click="editSonFormVisible=false">取 消</el-button>
          <el-button type="primary" @click="editSonFormButton()">确 定</el-button>
        </div>
      </el-dialog>

      <!-- 编辑子类方向对话框 -->
      <el-dialog :visible.sync="editSonDirectionsFormVisible">
        <el-form :inline="true" class="demo-form-inline" v-for="item in sonDirectionsFormArr.data" :key="item.index">
          <el-form-item label="名称">
            <el-input v-model="item.name"></el-input>
          </el-form-item>
          <el-form-item label="描述">
            <el-input v-model="item.desc"></el-input>
          </el-form-item>
          <el-button type="primary" @click="DeleteSonDirection(item.index)">删除</el-button>
        </el-form>
        <el-button type="primary" @click="AddSonDirectionForm">增加</el-button>

        <div slot="footer" class="dialog-footer">
          <el-button @click="editSonDirectionsFormVisible=false,editSonFormVisible=true">取 消</el-button>
          <el-button type="primary" @click="editSonDirectionFormButton()">确 定</el-button>
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
      addUserForm: {},
      // 添加用户对话框校验规则
      addUserFormRules: {
        name: [
          { required: true, message: '请输入名称', trigger: 'blur' },
          { min: 2, max: 32, message: '长度在 2 到 32 个字符', trigger: 'blur' }
        ],
      },
      editUserForm: {},
      // 子类列表
      editSonFormVisible: false,
      father_name: '',
      sonFormArr: [],
      // 子类方向列表
      editSonDirectionsFormVisible: false,
      sonIndex: 0,
      sonDirectionsFormArr: [],
    }
  },
  created () {
    this.getUsers(1, 10)
  },
  methods: {
    //获取列表
    async getUsers (page, page_size) {
      const res = await this.axios.get(
        `/projectCategory/?page=${page}&page_size=${page_size}`
      )
      if (res.status === 200) {
        this.users = res.data.results
        this.total = res.data.count
        // console.log(res)
      } else {
        this.$message.warning("错误")
      }
    },
    //分页
    handleSizeChange (val) {
      // console.log(`每页 ${val} 条`)
      this.page_size = val
      this.getUsers(this.currentPage, this.page_size)
    },
    handleCurrentChange (val) {
      // console.log(`当前页: ${val}`)
      this.currentPage = val
      this.getUsers(this.currentPage, this.page_size)
    },

    // 查询
    async queryUser () {
      const res = await this.axios.get(
        `/projectCategory/?page=${this.currentPage}&page_size=${this.page_size}&search=${this.query}`
      )
      if (res.status === 200) {
        this.users = res.data.results
        this.total = res.data.count
        // console.log(res)
      } else {
        this.$message.warning("错误")
      }
    },

    //添加
    showAddUserForm () {
      this.addUserFormVisible = true
    },

    async addUserFormButton () {
      const res = await this.axios.post("/projectCategory/", this.addUserForm)
      this.addUserFormVisible = false
      this.getUsers(this.currentPage, this.page_size)
    },

    // 编辑
    async showEditUserForm (id) {
      const res = await this.axios.get('/projectCategory/' + id)
      if (res.status !== 200) {
        return this.$message.error('查询课题类别信息失败！')
      }
      this.editUserForm = res.data
      this.editUserFormVisible = true
    },

    editUserFormButton () {
      this.$confirm("此操作将修改课题类别信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(async () => {
          var url = '/projectCategory/' + this.editUserForm.id + '/'
          // console.log(url)
          const res = await this.axios.put(url, this.editUserForm)
          if (res.status !== 200) {
            return this.$message.error('更新失败')
          }
          this.$message({
            type: "success",
            message: "修改成功!",
          })
          this.editUserFormVisible = false
          this.getUsers(this.currentPage, this.page_size)
        })
        .catch(() => {
          this.$message.error('更新失败')
        })
    },

    //删除
    deleteUser (row) {
      this.$confirm("此操作将永久删除信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(async () => {
          console.log('row', row)
          const resDel = await this.axios.delete(`/projectCategory/${row.id}`)
          // 删除子类
          let resSon = await this.axios.get('/projectCategorySon/?father_name=' + row.name)
          resSon = resSon.data.results
          for (let i = 0; i < resSon.length; i++) {
            let resDelSon = await this.axios.delete(`/projectCategorySon/${resSon[i].id}`)
          }
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

    //切换用户是否激活状态
    async categoryIsActive (row) {
      // console.log('row: ', row)
      var url = '/projectCategory/' + row.id + '/'
      var data = { name: row.name, is_active: row.is_active }
      const res = await this.axios.put(url, data)
      // const res = await this.axios.get(url)
      // console.log(res)
      if (res.status !== 200) {
        row.is_active = !row.is_active
        return this.$message.error('更新状态失败')
      }
      this.$message.success('更新状态成功！')
    },

    // 子类编辑
    async showEditSonForm (row) {
      this.editSonFormVisible = true
      this.sonFormArr = []
      this.father_name = row.name
      let url = '/projectCategorySon/?father_name=' + this.father_name
      let res = await this.axios.get(url)
      if (res.status === 200) {
        for (let i = 0; i < res.data.results.length; i++) {
          this.sonFormArr.push({
            index: i,
            name: res.data.results[i].name,
            desc: res.data.results[i].desc,
            father_name: this.father_name,
            // 表中direction为空报错，则赋值{"data":[]}
            direction: res.data.results[i].direction == null ?
              { "data": [] } : res.data.results[i].direction
          })
        }
        console.log('data', this.sonFormArr)
      }
    },
    AddSonForm () {
      this.sonFormArr.push({
        index: this.sonFormArr.length,
        father_name: this.father_name,
        name: '',
        desc: '',
        direction: { "data": [] }
      })
      // console.log(this.sonFormArr)
    },

    DeleteSon (index) {
      this.sonFormArr.splice(index, 1)
      for (let i in this.sonFormArr) {
        this.sonFormArr[i].index = i
      }
    },

    // 确定按钮，先删除，再添加
    async editSonFormButton () {
      // 删除
      let resDelete = await this.axios.get(`/projectCategorySon/?father_name=${this.father_name}`)
      let memberTemp = resDelete.data.results
      for (var i = 0; i < memberTemp.length; i++) {
        let res = await this.axios.delete(`/projectCategorySon/${memberTemp[i].id}/`)
      }
      // 增加      
      for (var i = 0; i < this.sonFormArr.length; i++) {
        let res = await this.axios.post(`/projectCategorySon/`, this.sonFormArr[i])
        if (res.status !== 201) {
          return this.$message.error('新增子类失败，请稍后再试')
        }
      }
      this.$message.success('保存成功')
      setTimeout(() => {
        this.editSonFormVisible = false
      }, 100);
    },

    // 编辑子类方向列表（第三层）
    EditSonDirection (index) {
      // console.log(this.sonFormArr[index])
      this.editSonFormVisible = false
      this.editSonDirectionsFormVisible = true
      this.sonIndex = index
      this.sonDirectionsFormArr = this.sonFormArr[index].direction
    },
    DeleteSonDirection (index) {
      this.sonDirectionsFormArr.data.splice(index, 1)
      for (let i in this.sonDirectionsFormArr.data) {
        this.sonDirectionsFormArr.data[i].index = i
      }
    },
    AddSonDirectionForm () {
      if (this.sonDirectionsFormArr.data == null) {
        this.sonDirectionsFormArr.data = []
      }
      this.sonDirectionsFormArr.data.push({
        index: this.sonDirectionsFormArr.data.length,
        name: '',
        desc: '',
      })
    },
    editSonDirectionFormButton () {
      this.editSonDirectionsFormVisible = false
      this.editSonFormVisible = true
      this.sonFormArr[this.sonIndex].direction = this.sonDirectionsFormArr
    },
  },
} 
</script>

<style>
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
.el-dialog {
  width: 60%;
}
</style>