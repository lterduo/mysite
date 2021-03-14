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
      <!-- <el-row class="row-search">
        <el-col class="el-col-user-add">
          <el-input class="user-search" clearable placeholder="请输申报书信息（用空格分隔），支持模糊搜索" v-model="query">
            <el-button slot="append" icon="el-icon-search" @click.prevent="queryProjectInfo()"></el-button>
          </el-input>
        </el-col>
      </el-row> -->
      <!-- 申报书列表 -->
      <el-table :data="projcetDistribute" style="width: 100%">
        <el-table-column type="index" label="序号" width="60"></el-table-column>
        <el-table-column prop="pname" label="名称" width="280"></el-table-column>
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
                  {{item.name}}
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
        <div class="divSuggestion">三、专家对该项目经费建议：</div>
        <el-input v-model="assessFunds"></el-input>
      </el-card>
      <el-card>
        <div class="divAgree">三、是否同意该项目立项：</div>
        <el-radio v-model="assessAgree" label="同意">是</el-radio>
        <el-radio v-model="assessAgree" label="不同意">否</el-radio>
      </el-card>
      <el-button type="primary" @click="assess()">提交</el-button>
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
      projcetDistribute: [],
      projectInfo: [],
      projectCategorys: [],
      selectValue: '', //课题类型下拉框显示的值
      infoFormVisible: false,
      editForm: {},  //编辑申报书
      fileList: [],  //附件列表
      // qill-editor
      editorOption: {},
      projectAssess: {}, //评审按钮传入的待评审课题
      //评审对话框
      assessDialogVisible: false,
      //评审评分信息
      assessScore:
        [
          {
            name: '1、研究内容与研究目标的一致性',
            scores: [
              { name: '很好', score: 5 },
              { name: '较好', score: 3 },
              { name: '一般', score: 2 },
              { name: '较差', score: 1 }],
            score: 0
          },
          {
            name: '2、研究路径、方法的科学性',
            scores: [
              { name: '很好', score: 5 },
              { name: '较好', score: 3 },
              { name: '一般', score: 2 },
              { name: '较差', score: 1 }],
            score: 0
          },
          {
            name: '3、项目的可行性',
            scores: [
              { name: '强', score: 5 },
              { name: '较强', score: 3 },
              { name: '一般', score: 2 },
              { name: '较差', score: 1 }],
            score: 0
          },
          {
            name: '4、前期的研究成果',
            scores: [
              { name: '高', score: 5 },
              { name: '较高', score: 3 },
              { name: '一般', score: 2 },
              { name: '较低', score: 1 }],
            score: 0
          },
          {
            name: '5、项目的团队力量',
            scores: [
              { name: '强', score: 5 },
              { name: '较强', score: 3 },
              { name: '一般', score: 2 },
              { name: '较差', score: 1 }],
            score: 0
          },
          {
            name: '6、项目时间安排的合理性',
            scores: [
              { name: '很好', score: 5 },
              { name: '较好', score: 3 },
              { name: '一般', score: 2 },
              { name: '较差', score: 1 }],
            score: 0
          },
          {
            name: '7、经费安排的合理性',
            scores: [
              { name: '很好', score: 5 },
              { name: '较好', score: 3 },
              { name: '一般', score: 2 },
              { name: '较差', score: 1 }],
            score: 0
          },
        ],
      // 评审建议
      assessSuggestion: '',
      assessFunds: 0,
      assessAgree: ''
    }
  },

  created () {
    this.userid = localStorage.getItem("userid")
    this.username = localStorage.getItem("username")
    this.getProjectInfo()
  },

  methods: {


    // 获取课题信息
    async getProjectInfo () {
      const res = await this.axios.get(`/projectDistribute/?assessor=${this.userid}`)
      if (res.status === 200) {
        this.projcetDistribute = res.data.results
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
      this.infoFormVisible = true
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

    //评审按钮
    assessButton (item) {
      this.assessDialogVisible = !this.assessDialogVisible
      this.projectAssess = item
    },

    // 计算评审结果
    async assess () {
      // console.log(this.assessScore)
      let score = 0
      for (let i = 0; i < this.assessScore.length; i++) {
        score = score + this.assessScore[i].score
      }
      // this.$message.success(`评审总分为：${score}分！`)
      let res = await this.axios.get('/projectAssess/?pid=' + this.projectAssess.pid)
      res = res.data.results

      // 写ProjectAssess评审结果表
      if (res[0]) {
        // 有记录,添加记录的assessor_result
        let data = res[0]
        // 将评审结果添加到数组
        data.assessor_result.data.push(
          {
            assessor: this.userid,
            aname: this.username,
            assessSuggestion: this.assessSuggestion,
            assessAgree: this.assessAgree,
            assessScore: this.assessScore,
            total_score: score,
            assessFunds: this.assessFunds
          }
        )
        let resPut = await this.axios.put(`/projectAssess/${data.id}/`, data)
        // 删除projectDistribute
        let resGet = await this.axios.get('/projectDistribute/?pid=' + this.projectAssess.pid + '&assessor=' + this.userid)
        resGet = resGet.data.results[0]
        let resDel = await this.axios.delete(`/projectDistribute/${resGet.id}`)
        console.log('del:' + resDel.data.status)
        if (resPut.status == 200) {
          this.$message.success('评审完成')
        } else {
          this.$message.error('评审失败')
        }
      } else {
        // 无记录，post
        let data = {
          pid: this.projectAssess.pid,
          pname: this.projectAssess.pname,
          status: 1,
          assessor_result: {
            data: [{
              assessor: this.userid,
              aname: this.username,
              assessSuggestion: this.assessSuggestion,
              assessAgree: this.assessAgree,
              assessScore: this.assessScore,
              total_score: score,
              assessFunds: this.assessFunds
            }]
          }
        }
        let resPost = await this.axios.post('/projectAssess/', data)
        // 删除projectDistribute
        let resGet = await this.axios.get('/projectDistribute/?pid=' + this.projectAssess.pid + '&assessor=' + this.userid)
        resGet = resGet.data.results[0]
        let resDel = await this.axios.delete(`/projectDistribute/${resGet.id}`)
        console.log('del:' + resDel.data.status)
        if (resPost.status == 201) {
          this.$message.success('评审成功！')
        } else {
          this.$message.error('评审失败')
        }
      }
      // 对话框不可见，初始化课题列表
      this.assessDialogVisible = false
      this.getProjectInfo()
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