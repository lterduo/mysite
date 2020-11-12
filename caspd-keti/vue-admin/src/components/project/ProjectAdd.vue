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
            <el-button slot="append" icon="el-icon-search" @click.prevent="queryProjectInfo()"></el-button>
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
              :disabled="(scope.row.status==1 || scope.row.status==3)?false:true" @click="showEditForm(scope.row.id)">
            </el-button>
            <!-- 只有状态为1（待提交）或3（待修改）的才能点击修改按钮 -->
          </template>
        </el-table-column>
      </el-table>

    </el-card>
    <!-- 申报书新增 -->
    <el-card v-show="addFormVisible">
      <el-col>
        <div class="header-edit">新增申报书</div>
      </el-col>
      <el-card>
        <el-col class="el-col-addForm">
          <span> 课题类别：</span>
          <el-select v-model="addForm.category" filterable allow-create default-first-option placeholder="请选择课题类别">
            <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
            </el-option>
          </el-select>
          <span> 课题名称：</span>
          <el-input v-model="addForm.name"></el-input>
        </el-col>
      </el-card>
      <el-card class="el-card-leader">
        <div class="div-leader">
          <span>项目主持人情况</span>
          <el-button type="success" plain style="margin-left: 10px;" @click="showEditLeader()">修改信息</el-button>
        </div>
        <el-table :data="projectLeader" border style="width:1021px;" :header-cell-style="{background:'#fafafa'}">
          <el-table-column prop="name" label="姓名" width="80"></el-table-column>
          <el-table-column prop="gender" label="性别" width="60"></el-table-column>
          <el-table-column prop="national" label="民族" width="80"></el-table-column>
          <el-table-column prop="birth" label="出生年月" width="80"></el-table-column>
          <el-table-column prop="duty" label="行政职务" width="120"></el-table-column>
          <el-table-column prop="title" label="专业职称" width="120"></el-table-column>
          <el-table-column prop="major" label="研究专长" width="140"></el-table-column>
          <el-table-column prop="education" label="最后学历" width="80"></el-table-column>
          <el-table-column prop="degree" label="最后学位" width="80"></el-table-column>
          <el-table-column prop="province" label="所在省(自治区、直辖市)" width="180"></el-table-column>
        </el-table>
        <el-table :data="projectLeader" border style="width:1021px; margin-top:-1px;"
          :header-cell-style="{background:'#fafafa'}">
          <el-table-column prop="organization" label="工作单位" width="280"></el-table-column>
          <el-table-column prop="tel" label="联系电话" width="160"></el-table-column>
          <el-table-column prop="email" label="E-mail" width="200"></el-table-column>
          <el-table-column prop="addr" label="通讯地址" width="280"></el-table-column>
          <el-table-column prop="zipcode" label="邮政编码" width="100"></el-table-column>
        </el-table>
      </el-card>
      <el-card>
        <div class="member">
          <span> 主要参加者情况</span>
          <el-button type="success" plain style="margin-left: 10px;" @click="showAddMember()">新增参加者</el-button>
        </div>
        <el-table :data="projectMember" border style="width:1021px;" :header-cell-style="{background:'#fafafa'}">
          <el-table-column prop="name" label="姓名" width="80"></el-table-column>
          <el-table-column prop="organization" label="单位" width="280"></el-table-column>
          <el-table-column prop="education" label="最后学历" width="80"></el-table-column>
          <el-table-column prop="major" label="所学专业" width="160"></el-table-column>
          <el-table-column prop="duty" label="技术职务" width="120"></el-table-column>
          <el-table-column prop="division" label="研究分工" width="200"></el-table-column>
          <el-table-column label="操作" width="100">
            <template slot-scope="scope">
              <el-button size="mini" :plain="true" type="primary" icon="el-icon-edit" circle
                @click="showEditMember(scope.$index, scope.row)"></el-button>
              <el-button size="mini" :plain="true" type="danger" icon="el-icon-delete" circle
                @click="deleteMemberButton(scope.$index, scope.row)"></el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
      <el-card>
        <el-row class="el-row-detail">
          <el-col :span="8"><span> 预期成果形式：</span>
            <el-input v-model="addForm.result_type"></el-input>
          </el-col>
          <el-col :span="8"><span> 字数：</span>
            <el-input v-model="addForm.total_words"></el-input>
          </el-col>
          <el-col :span="8"><span> 预计完成时间：</span>
            <el-input v-model="addForm.complete_time"></el-input>
          </el-col>
        </el-row>
      </el-card>
      <el-card>
        <div>课题研究计划</div>
        <quill-editor v-model="addForm.content" class="editor"></quill-editor>
      </el-card>
      <!-- 保存按钮 -->
      <div class="div-add">
        <el-button type="primary" @click.prevent="addProject()" class="el-button-add">保存</el-button>
        <el-button type="primary" @click.prevent="addProject()" class="el-button-add">提交审核</el-button>
      </div>
    </el-card>

    <!-- 申报书修改 -->
    <el-card v-show="editFormVisible">
      <el-row>
        <el-col :span="24">
          <div class="header-edit">修改申报书</div>
        </el-col>
      </el-row>
    </el-card>

    <!-- 对话框 -->
    <!-- 编辑主持人对话框 -->
    <el-dialog title="编辑主持人信息" :visible.sync="editLeaderVisible">
      <el-form label-position="right" label-width="180px" :model="leader" :rules="leaderRules" class="demo-ruleForm">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="leader.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="gender">
          <el-input v-model="leader.gender" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="民族" prop="national">
          <el-input v-model="leader.national" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="出生年月" prop="birth">
          <el-input v-model="leader.birth" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="行政职务" prop="duty">
          <el-input v-model="leader.duty" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="专业职称" prop="title">
          <el-input v-model="leader.title" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="研究专长" prop="major">
          <el-input v-model="leader.major" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最后学历" prop="education">
          <el-input v-model="leader.education" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最后学位" prop="degree">
          <el-input v-model="leader.degree" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所在省(自治区、直辖市)" prop="province">
          <el-input v-model="leader.province" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="工作单位" prop="organization">
          <el-input v-model="leader.organization" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="联系电话" prop="tel">
          <el-input v-model="leader.tel" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="E-mail" prop="email">
          <el-input v-model="leader.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="通讯地址" prop="addr">
          <el-input v-model="leader.addr" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮政编码" prop="zipcode">
          <el-input v-model="leader.zipcode" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editLeaderVisible=false">取 消</el-button>
        <el-button type="primary" @click="editLeader()">确 定</el-button>
      </div>
    </el-dialog>
    <!-- 新增参加者对话框 -->
    <el-dialog title="新增参加者信息" :visible.sync="addMemberVisible">
      <el-form label-position="right" label-width="80px" :model="addMember" :rules="memberRules">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="addMember.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="单位" prop="organization">
          <el-input v-model="addMember.organization" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最后学历" prop="education">
          <el-input v-model="addMember.education" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所学专业" prop="major">
          <el-input v-model="addMember.major" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="技术职务" prop="duty">
          <el-input v-model="addMember.duty" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="研究分工" prop="division">
          <el-input v-model="addMember.division" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addMemberVisible=false">取 消</el-button>
        <el-button type="primary" @click="addMemberButton()">确 定</el-button>
      </div>
    </el-dialog>
    <!-- 编辑参加者对话框 -->
    <el-dialog title="编辑参加者信息" :visible.sync="editMemberVisible">
      <el-form label-position="right" label-width="80px" :model="addMember" :rules="memberRules">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="addMember.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="单位" prop="organization">
          <el-input v-model="addMember.organization" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最后学历" prop="education">
          <el-input v-model="addMember.education" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="所学专业" prop="major">
          <el-input v-model="addMember.major" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="技术职务" prop="duty">
          <el-input v-model="addMember.duty" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="研究分工" prop="division">
          <el-input v-model="addMember.division" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="editMemberButton()">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
//富文本
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import { quillEditor } from 'vue-quill-editor'

export default {
  components: {
    quillEditor
  },
  data () {
    return {
      pid: '',
      userid: '',
      query: '',  //查询条件
      projectInfo: [],
      projectCategorys: {},
      projectStatus: [],
      status: '',
      projectLeader: [],  //主持人，返回的是列表
      leader: {}, //主持人，取列表第一项
      projectMember: [],  //本项目参加人
      addFormVisible: false,  //显示新增卡片      
      addForm: {},
      editFormVisible: false, // 显示编辑卡片
      editForm: {},
      editLeaderVisible: false,  //显示编辑主持人对话框
      addMemberVisible: false,  //显示新增参加人对话框
      addMember: {},  //新增参加人信息（编辑参加人也用）
      editMemberVisible: false,  //显示编辑参加者对话
      leaderRules: {
        name: [{ required: true, message: '姓名不能为空', trigger: 'blur' },],
        gender: [{ required: true, message: '性别不能为空', trigger: 'blur' },],
        national: [{ required: true, message: '民族不能为空', trigger: 'blur' },],
        birth: [{ required: true, message: '出生年月不能为空', trigger: 'blur' },],
        duty: [{ required: true, message: '行政职务不能为空', trigger: 'blur' },],
        title: [{ required: true, message: '专业职称不能为空', trigger: 'blur' },],
        major: [{ required: true, message: '研究专长不能为空', trigger: 'blur' },],
        education: [{ required: true, message: '最后学历不能为空', trigger: 'blur' },],
        degree: [{ required: true, message: '最后学位不能为空', trigger: 'blur' },],
        province: [{ required: true, message: '所在省(自治区、直辖市)不能为空', trigger: 'blur' },],
        organization: [{ required: true, message: '工作单位不能为空', trigger: 'blur' },],
        tel: [{ required: true, message: '联系电话不能为空', trigger: 'blur' },],
        email: [{ required: true, message: 'E-mail不能为空', trigger: 'blur' },],
        addr: [{ required: true, message: '通讯地址不能为空', trigger: 'blur' },],
        zipcode: [{ required: true, message: '邮政编码不能为空', trigger: 'blur' },],
      },  //主持人input规则
      memberRules: {
        name: [{ required: true, message: '姓名不能为空', trigger: 'blur' },],
        organization: [{ required: true, message: '单位不能为空', trigger: 'blur' },],
        education: [{ required: true, message: '最后学历不能为空', trigger: 'blur' },],
        major: [{ required: true, message: '所学专业不能为空', trigger: 'blur' },],
        duty: [{ required: true, message: '技术职务不能为空', trigger: 'blur' },],
        division: [{ required: true, message: '研究分工不能为空', trigger: 'blur' },],
      },  //参加者input规则
    }
  },
  created () {
    this.getProjectCategorys()
    this.userid = localStorage.getItem("userid")
    this.getProjectInfo()
    this.getProjectStatus()
    //创建pid
    this.pid = this.userid + (new Date).getTime().toString()
    console.log('pid:  ', this.pid)
    //leader member 测试用，不能放这里
    this.getProjectLeader()
    this.getProjectMember(1)
  },
  methods: {
    //获取课题类别
    async getProjectCategorys () {
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
    async queryProjectInfo () {
      const res = await this.axios.get(`/projectInfo/?leader=${this.userid}&search=${this.query}`)
      if (res.status === 200) {
        this.projectInfo = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    // 查询主持人信息
    async getProjectLeader () {
      const res = await this.axios.get(`/projectLeader/?userid=${this.userid}`)
      if (res.status === 200) {
        this.projectLeader = res.data.results
        this.leader = this.projectLeader[0]
      } else {
        this.$message.warning("错误")
      }
    },

    // 修改主持人信息
    showEditLeader () {
      this.editLeaderVisible = true
    },
    editLeader () {
      this.$confirm("此操作将修改用户信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(async () => {
          const res = await this.axios.put(`/projectLeader/${this.leader.id}/`, this.leader)
          if (res.status !== 200) {
            return this.$message.error('更新用户状态失败')
          }
          this.$message.success('修改成功!')
          this.editLeaderVisible = false
        })
        .catch(() => {
          this.$message.error('修改失败')
        })
    },

    // 查询参加者
    async getProjectMember (id) {
      const res = await this.axios.get(`/projectMember/?pid=${id}`)
      console.log(this.userid)
      if (res.status === 200) {
        this.projectMember = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    // 新增参加者
    showAddMember () {
      this.addMemberVisible = true
      this.addMember = {}
    },
    addMemberButton () {
      this.projectMember.push(this.addMember)
      this.addMemberVisible = false
      console.log('addMember:  ', this.addMember)
      this.addMember = {}
    },

    // 修改参加者
    showEditMember (index) {
      this.editMemberVisible = true
      this.addMember = this.projectMember[index]
    },
    editMemberButton () {
      this.editMemberVisible = false
    },

    // 删除参加者
    deleteMemberButton (index) {
      this.projectMember.splice(index, 1)
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
          name = s.status
        }
      })
      return name
    },

    // 新增申报书
    addProject () {
      console.log('addForm:  ', this.addForm)
      console.log(this.projectLeader)
      console.log(this.projectMember)
    },

    // 测试
    test () {
      this.editFormVisible = !this.editFormVisible
    },
  },
}
</script>

<style lang="less">
.el-card {
  margin-top: 15px;
}
.header-edit {
  font-size: 18px;
  text-align: left;
  margin-bottom: 20px;
}
.el-col-user-add {
  display: flex;
}
.user-search {
  width: 420px;
  margin-right: 10px;
}
.el-col-addForm {
  display: flex;
  margin-bottom: 20px;
  span {
    display: flex;
    align-items: center;
    margin-left: 10px;
  }
  .el-input {
    width: 400px;
  }
}
.el-card-leader {
  .div-leader {
    font-size: 16px;
    margin-bottom: 15px;
  }
}
.member {
  font-size: 16px;
  margin-bottom: 15px;
}
.el-row-detail {
  width: 1020px;
  .el-col {
    display: flex;
    span {
      display: flex;
      align-items: center;
      margin-left: 10px;
    }
    .el-input {
      width: 200px;
    }
  }
}
.editor {
  margin-top: 15px;
}
.ql-editor {
  height: 200px;
}
.div-add {
  margin-top: 20px;
  display: flex;
  justify-content: end;
}
</style>