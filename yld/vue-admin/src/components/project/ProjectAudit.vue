<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>申报书管理</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>申报书审核</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 搜索框 新增按钮-->
      <el-row class="row-search">
        <el-col class="el-col-user-add">
          <el-input class="user-search" clearable placeholder="请输申报书信息（用空格分隔），支持模糊搜索" v-model="query">
            <el-button slot="append" icon="el-icon-search" @click.prevent="queryProjectInfo()"></el-button>
          </el-input>
        </el-col>
      </el-row>
      <!-- 申报书列表 -->
      <el-table :data="projectInfo" style="width: 100%">
        <el-table-column type="index" label="序号" width="60"></el-table-column>
        <el-table-column prop="name" label="名称" width="280"></el-table-column>
        <el-table-column prop="category" label="类别" width="280">
          <template slot-scope="scope">
            <div>{{categoryName(scope.row.category)}}</div>
          </template>
        </el-table-column>
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
        <el-table-column label="操作" width="150">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-search" circle
              @click="showInfoForm(scope.row)">
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 申报书查看 -->
    <el-card v-show="infoFormVisible" id="id-el-card-info">
      <el-row>
        <el-col :span="24">
          <div class="header-edit">申报书详情</div>
        </el-col>
      </el-row>
      <el-card>
        <el-col class="el-col-addForm">
          <span> 课题类别方向：</span>
          <el-select :disabled="true" v-model="selectValue" filterable allow-create default-first-option
            placeholder="请选择课题类别">
            <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
            </el-option>
          </el-select>
          <span> 课题名称：</span>
          <el-input :disabled="true" v-model="editForm.name"></el-input>
        </el-col>
      </el-card>
      <!-- 项目主持人情况 -->
      <el-card class="el-card-leader">
        <div class="div-leader">
          <span>项目主持人情况</span>
        </div>
        <el-table :data="projectLeader" border style="width:1021px;" :header-cell-style="{background:'#fafafa'}">
          <el-table-column prop="username" label="姓名" width="80"></el-table-column>
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
      <!-- 主要参加者情况 -->
      <el-card>
        <div class="member">
          <span> 主要参加者情况</span>
        </div>
        <el-table :data="projectMember" style="width:1021px;" :header-cell-style="{background:'#fafafa'}">
          <el-table-column prop="name" label="姓名" width="80"></el-table-column>
          <el-table-column prop="organization" label="单位" width="280"></el-table-column>
          <el-table-column prop="education" label="最后学历" width="80"></el-table-column>
          <el-table-column prop="major" label="所学专业" width="160"></el-table-column>
          <el-table-column prop="duty" label="技术职务" width="120"></el-table-column>
          <el-table-column prop="division" label="研究分工" width="200"></el-table-column>
        </el-table>
      </el-card>
      <!-- 预期成果形式 -->
      <el-card>
        <el-row class="el-row-detail">
          <el-col :span="8"><span> 预期成果形式：</span>
            <el-input :disabled="true" v-model="editForm.result_type"></el-input>
          </el-col>
          <el-col :span="8"><span> 字数：</span>
            <el-input :disabled="true" v-model="editForm.total_words"></el-input>
          </el-col>
          <el-col :span="8"><span> 预计完成时间：</span>
            <el-input :disabled="true" v-model="editForm.complete_time"></el-input>
          </el-col>
        </el-row>
      </el-card>
      <!-- 课题研究计划 -->
      <el-card>
        <div>课题研究计划</div>
        <quill-editor :disabled="true" v-model="editForm.content" :options="editorOption" class="editor"></quill-editor>
        <!-- 文件列表 -->
        <div class="div-file">
          <el-table :data="fileList" style="width:551px;" :header-cell-style="{background:'#fafafa'}">
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
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-card>
      <!-- 审核 -->
      <el-card>
        <div>填写审核意见或通过审核</div>
        <quill-editor v-model="auditInfo.info" :options="editorOption" class="editor"></quill-editor>
        <div class="div-add">
          <el-button type="primary" @click.prevent="auditAdvice()" class="el-button-add">提交审核意见</el-button>
          <el-button type="primary" @click.prevent="auditSubmit()" class="el-button-add">审核通过</el-button>
        </div>
      </el-card>
    </el-card>

  </div>
</template>

<script>

//富文本
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import * as Quill from 'quill'
import { quillEditor } from 'vue-quill-editor'
import { ImageDrop } from 'quill-image-drop-module'
import ImageResize from 'quill-image-resize-module'
Quill.register('modules/imageDrop', ImageDrop);
Quill.register('modules/imageResize', ImageResize);

//下载
import fileDownload from 'js-file-download'

export default {
  components: {
    quillEditor
  },
  data () {
    return {
      editContent: '',
      pid: '',
      userid: '',
      query: '',  //查询条件
      projectInfo: [],
      projectCategorys: [],
      selectValue: '', //课题类型下拉框显示的值
      projectStatus: [],
      status: '',
      projectLeader: [],  //主持人，返回的是列表
      leader: {}, //主持人，取列表第一项
      projectMember: [],  //本项目参加人
      addFormVisible: false,  //显示新增卡片      
      addForm: {},
      infoFormVisible: false,
      editForm: {},  //编辑申报书
      editFormVisible: false, // 显示编辑卡片
      auditInfo: {},
      editLeaderVisible: false,  //显示编辑主持人对话框
      addMemberVisible: false,  //显示新增参加人对话框
      addMember: {},  //新增参加人信息（编辑参加人也用）
      editMemberVisible: false,  //显示编辑参加者对话
      fileList: [],  //附件列表
      // qill-editor
      editorOption: {
        modules: {
          imageDrop: true,      //图片拖拽
          imageResize: {          //放大缩小
            displaySize: true
          },
          toolbar: [
            ["bold", "italic", "underline", "strike"], // 加粗 斜体 下划线 删除线
            ["blockquote", "code-block"], // 引用  代码块
            [{ header: 1 }, { header: 2 }], // 1、2 级标题
            [{ list: "ordered" }, { list: "bullet" }], // 有序、无序列表
            [{ script: "sub" }, { script: "super" }], // 上标/下标
            [{ indent: "-1" }, { indent: "+1" }], // 缩进
            // [{'direction': 'rtl'}],                         // 文本方向
            [{ size: ["small", false, "large", "huge"] }], // 字体大小
            [{ header: [1, 2, 3, 4, 5, 6, false] }], // 标题
            [{ color: [] }, { background: [] }], // 字体颜色、字体背景颜色
            [{ font: [] }], // 字体种类
            [{ align: [] }], // 对齐方式
            ["clean"], // 清除文本格式
            ["link", "image", "video"] // 链接、图片、视频
          ], //工具菜单栏配置
        },
        placeholder: '请在这里填写审核信息', //提示
        readyOnly: false, //是否只读
        theme: 'snow', //主题 snow/bubble
      },
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
  },

  methods: {

    // 获取审核信息
    async getAuditInfo (pid) {
      this.auditInfo.auditor = localStorage.getItem('userid')
      try {
        const res = await this.axios.get(`/auditInfo/?pid=${pid}`)
        if (res.status === 200) {
          if (res.data.results[0]) {
            this.auditInfo = res.data.results[0]
          }
        }
      } catch (err) {
        console.log(err)
      }
    },

    // 审核意见
    async auditAdvice () {
      try {
        let resget = await this.axios.get(`/auditInfo/?pid=${this.editForm.pid}`)
        if (resget.status === 200) {
          if (resget.data.results[0]) {
            let id = resget.data.results[0].id
            let resdelete = await this.axios.delete(`/auditInfo/${id}/`)
          }
        }
      } catch (err) {
        console.log(err)
      }
      this.auditInfo.pid = this.editForm.pid
      this.auditInfo.auditor = localStorage.getItem("userid")
      let res = await this.axios.post(`/auditInfo/`, this.auditInfo)
      if (res.status === 201) {
      } else {
        this.$message.warning("错误")
      }
      this.editForm.status = 3
      try {
        await this.axios.put(`/projectInfo/${this.editForm.id}/`, this.editForm)
      } catch (err) {
        console.log(err)
      }
      setTimeout(() => {
        location.reload()
      }, 500)
    },

    // 审核通过
    async auditSubmit () {
      try {
        this.editForm.status = 4
        let resget = await this.axios.put(`/projectInfo/${this.editForm.id}/`, this.editForm)
      } catch (err) {
        console.log(err)
      }
      setTimeout(() => {
        location.reload()
      }, 500)
    },

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
      } else {
        this.$message.warning("错误")
      }
    },

    // 获取课题信息
    async getProjectInfo () {
      const res = await this.axios.get(`/projectInfo/?status=2`)
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

    // 获取附件列表
    async getFileList (pid) {
      const res = await this.axios.get(`/fileList/?pid=${pid}`)
      if (res.status === 200) {
        this.fileList = res.data.results
      } else {
        this.$message.warning("获取文件列表错误")
      }
    },

    // 查询主持人信息
    async getProjectLeader () {
      const res = await this.axios.get(`/user/?userid=${this.userid}`)
      if (res.status === 200) {
        this.projectLeader = res.data.results
        this.leader = this.projectLeader[0]
      } else {
        this.$message.warning("错误")
      }
    },

    // 查询参加者
    async getProjectMember (id) {
      const res = await this.axios.get(`/projectMember/?pid=${id}`)
      if (res.status === 200) {
        this.projectMember = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    //获取状态名称
    statusName (id) {
      name = ''
      this.projectStatus.forEach((s) => {
        if (s.s_id == id) {
          name = s.status
        }
      })
      return name
    },

    // 获取类别名称
    categoryName (id) {
      const item = this.projectCategorys.find(item => item.id == id)
      return item ? item.name : null
    },

    // 显示查看申报书卡片（）
    showInfoForm (item) {
      this.infoFormVisible = true
      this.addFormVisible = false
      this.editFormVisible = false
      this.editForm = item
      this.selectValue = this.categoryName(this.editForm.category) //讲id转换成文字
      this.getProjectMember(item.pid)
      this.getFileList(item.pid)
      this.getAuditInfo(item.pid)

      setTimeout(() => {
        document.getElementById("id-el-card-info").scrollIntoView({ behavior: "smooth" })
      }, 500);
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
}
</script>

<style lang="less">
.el-card {
  margin-top: 15px;
}
.header-edit {
  font-size: 18px;
  text-align: left;
  margin-bottom: 10px;
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
  margin-bottom: 10px;
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
  min-height: 200px;
}
.div-upload {
  width: 500px;
  padding-top: 10px;
}
.div-add {
  margin-top: 20px;
  display: flex;
  justify-content: end;
}
.div-file {
  margin-top: 15px;
}
</style>