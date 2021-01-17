<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>立项评审</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>课题评审</el-breadcrumb-item>
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
        <el-table-column label="查看" width="80">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-search" circle
              @click="showInfoForm(scope.row)">
            </el-button>
          </template>
        </el-table-column>
        <el-table-column label="评审" width="150">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" @click="assessButton(scope.row)">评审
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
          <span> 课题类别：</span>
          <el-select :disabled="true" v-model="selectValue" filterable allow-create default-first-option
            placeholder="请选择课题类别">
            <el-option v-for="item in projectCategorys" :key="item.id" :label="item.name" :value="item.id">
            </el-option>
          </el-select>
          <span> 课题名称：</span>
          <el-input :disabled="true" v-model="editForm.name"></el-input>
        </el-col>
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
    </el-card>
    <!-- 评审对话框 -->
    <el-dialog title="课题评审" :visible.sync="assessDialogVisible">
      <el-card>
        <div class="divScore">一、专家对科研项目的基本评定（请点击相应的评分）：</div>
        <el-table :data="assessScore">
          <el-table-column prop="name" label="评分项"></el-table-column>
          <el-table-column prop="score" label="评分" width="500">
            <template slot-scope="scope">
              <el-radio-group v-model="scope.row.score" v-for="item in scope.row.scores" :key=item.score>
                <el-radio :label="item.score">
                  {{item.score}}
                </el-radio>
              </el-radio-group>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
      <el-card>
        <div class="divSuggestion">二、专家对该项目的意见及建议：</div>
        <el-input type="textarea" v-model="assessSuggestion"></el-input>
      </el-card>
      <el-card>
        <div class="divAgree">三、是否同意该项目立项：</div>
        <el-radio-group v-model="assessAgree">
          <el-radio :label="true">是</el-radio>
          <el-radio :label="false">否</el-radio>
        </el-radio-group>
      </el-card>
      <el-button type="primary">提交</el-button>
    </el-dialog>
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
      infoFormVisible: false,
      editForm: {},  //编辑申报书
      fileList: [],  //附件列表
      // qill-editor
      editorOption: {},
      //评审对话框
      assessDialogVisible: false,
      //评审评分信息
      assessScore:
        [
          {
            name: '1、研究内容与研究目标的一致性',
            scores: [
              { score: '很好' },
              { score: '较好' },
              { score: '一般' },
              { score: '较差' }],
            score: ''
          },
          {
            name: '2、研究路径、方法的科学性',
            scores: [
              { score: '很好' },
              { score: '较好' },
              { score: '一般' },
              { score: '较差' }],
            score: ''
          },
          {
            name: '3、项目的可行性',
            scores: [
              { score: '强' },
              { score: '较强' },
              { score: '一般' },
              { score: '较差' }],
            score: ''
          },
          {
            name: '4、前期的研究成果',
            scores: [
              { score: '高' },
              { score: '较高' },
              { score: '一般' },
              { score: '较低' }],
            score: ''
          },
          {
            name: '5、项目的团队力量',
            scores: [
              { score: '强' },
              { score: '较强' },
              { score: '一般' },
              { score: '较差' }],
            score: ''
          },
          {
            name: '6、项目时间安排的合理性',
            scores: [
              { score: '很好' },
              { score: '较好' },
              { score: '一般' },
              { score: '较差' }],
            score: ''
          },
          {
            name: '7、经费安排的合理性',
            scores: [
              { score: '很好' },
              { score: '较好' },
              { score: '一般' },
              { score: '较差' }],
            score: ''
          },
        ],
      // 评审建议
      assessSuggestion: '',
      assessAgree: ''
    }
  },

  created () {
    this.getProjectCategorys()
    this.getProjectCategorySon()
    this.userid = localStorage.getItem("userid")
    this.getProjectInfo()
  },

  methods: {

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
      const res = await this.axios.get(`/projectInfo/?status=5`)
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

    //获取课题类别
    async getProjectCategorys () {
      const res1 = await this.axios.get(`/projectCategory/?is_active=True`)
      if (res1.status === 200) {
        if (res1.data.results.length === 1) {
          this.projectCategory = res1.data.results[0].name
          //获取课题类别方向
          this.getProjectCategorySon()
        } else {
          this.$message.warning(`存在${res1.data.results.length}个激活类型，请联系管理员修改！`)
        }
      } else {
        this.$message.warning("获取类型错误")
      }
    },

    // 获取课题类别方向
    async getProjectCategorySon () {
      const res = await this.axios.get(`/projectCategorySon/?father_name=${this.projectCategory}`)
      if (res.status === 200) {
        this.projectCategorySon = res.data.results
      } else {
        this.$message.warning("错误")
      }
    },

    // 获取类别名称
    categoryName (id) {
      const item = this.projectCategorySon.find(item => item.id == id)
      return item ? item.name : null
    },

    // 显示查看申报书卡片（）
    showInfoForm (item) {
      this.infoFormVisible = true
      this.editForm = item
      this.selectValue = this.categoryName(this.editForm.category) //讲id转换成文字
      this.getFileList(item.pid)

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

    //评审按钮
    assessButton () {
      this.assessDialogVisible = !this.assessDialogVisible
    }
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
.el-dialog {
  .divScore {
    font-size: 20px;
  }
  .el-radio {
    margin-left: 20px;
    width: 70px;
  }
  .divSuggestion {
    font-size: 20px;
    margin-bottom: 20px;
  }
  .divAgree {
    font-size: 20px;
    margin-bottom: 20px;
  }
  .el-button {
    margin-top: 30px;
  }
}
</style>