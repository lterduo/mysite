<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>立项评审</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>管理员计算</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <!-- 申报书列表 -->
      <el-table :data="projectAssess" style="width: 100%">
        <el-table-column type="index" label="序号" width="60"></el-table-column>
        <el-table-column prop="pid" label="课题编号" width="280"></el-table-column>
        <el-table-column prop="pname" label="课题名称" width="280"></el-table-column>
        <el-table-column label="查看" width="80">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-search" circle
              @click="showInfoForm(scope.row)">
            </el-button>
          </template>
        </el-table-column>
        <el-table-column label="计算" width="150">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="primary" @click="assessButton(scope.row)">计算
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
          <el-input :disabled="true" v-model="editForm.category_direction"></el-input>
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
    <el-card v-show="computeCardVisible">
      <el-table :data="assessResult.data" style="width: 100%">
        <el-table-column prop="aname" label="专家" width="180"></el-table-column>
        <el-table-column prop="assessAgree" label="是否同意" width="110"></el-table-column>
        <el-table-column prop="total_score" label="打分" width="80"></el-table-column>
        <!-- 打分详情 -->
        <el-table-column type="expand" label="展开" width="80">
          <template slot-scope="scope">
            <el-table :data="scope.row.assessScore">
              <el-table-column prop="name" label="评分项"></el-table-column>
              <el-table-column prop="score" label="得分"></el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <el-table-column prop="assessFunds" label="经费" width="180"></el-table-column>
        <el-table-column prop="assessSuggestion" label="评审意见" width="280"></el-table-column>
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <el-button size="mini" :plain="true" type="danger" icon="el-icon-delete" circle
              @click="deleteAssessResult(scope.row)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="div-compute">
        <span>评审专家总数：{{computeResult.assessors}}</span>
        <span>同意数：{{computeResult.agrees}}</span>
        <span>总分：{{computeResult.score}}</span>
        <span>平均经费：{{computeResult.assessFunds}}</span>
      </div>
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
      infoFormVisible: false,
      editForm: {},  //编辑申报书
      fileList: [],  //附件列表
      // qill-editor
      editorOption: {},
      projectAssess: [], //课题列表
      computeCardVisible: false,
      assessResult: {},  //专家评审详情
      computeResult: {},
      projectAssessUpdate: {}, //删除某专家评审意见时用,更新projectAssess
    }
  },

  created () {
    this.userid = localStorage.getItem("userid")
    this.getProjectInfo()
  },

  methods: {

    // 获取课题信息
    async getProjectInfo () {
      // 查询status为1（专家已评审）的项目
      const res = await this.axios.get(`/projectAssess/?status=1`)
      if (res.status === 200) {
        this.projectAssess = res.data.results
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


    // 显示查看申报书卡片（）
    async showInfoForm (item) {
      this.infoFormVisible = !this.infoFormVisible
      let res = await this.axios.get('/projectInfo/?pid=' + item.pid)
      this.editForm = res.data.results[0]
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

    //计算按钮
    assessButton (item) {
      this.infoFormVisible = false
      this.computeCardVisible = true
      this.assessResult = item.assessor_result
      // 传入pid，delete某专家评审结果时需要
      this.projectAssessUpdate = item
      console.log(this.projectAssessUpdate)
      let agrees = 0
      let score = 0
      let assessFunds = 0
      for (let i = 0; i < this.assessResult.data.length; i++) {
        score = score + this.assessResult.data[i].total_score
        if (this.assessResult.data[i].assessAgree == '同意') {
          agrees = agrees + 1
        }
        // 经费累加
        if (this.assessResult.data[i].assessFunds) {
          assessFunds = assessFunds + this.assessResult.data[i].assessFunds
        }
      }
      // 平均经费
      assessFunds = assessFunds / this.assessResult.data.length
      this.computeResult = {
        assessors: this.assessResult.data.length,
        agrees: agrees,
        score: score,
        assessFunds: assessFunds
      }
    },

    // 删除某个评审结果（通知专家重新评审）
    async deleteAssessResult (item) {
      // 删除评审结果
      for (let i = 0; i < this.assessResult.data.length; i++) {
        if (item == this.assessResult.data[i]) {
          console.log(item)
          this.assessResult.data.splice(i, 1)
        }
      }
      // 更新评审表
      this.projectAssessUpdate.assessor_result = this.assessResult
      let id = this.projectAssessUpdate.id
      let resPut = await this.axios.put(`/projectAssess/${id}/`, this.projectAssessUpdate)
      console.log(resPut)
      // 添加分配表，重新评审
      let dataTemp = {
        pid: this.projectAssessUpdate.pid,
        pname: this.projectAssessUpdate.pname,
        assessor: item.assessor,
        aname: item.aname
      }
      let resPost = await this.axios.post('/projectDistribute/', dataTemp)
      console.log(resPost)
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
.div-compute {
  margin-top: 20px;
  span {
    margin-right: 20px;
  }
}
</style>