<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>申报书分配</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>申报书分配</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card>
      <el-row :gutter="20">
        <el-col :span="12">
          <div class="projectList">
            <div>
              <span> 课题类别：</span>
              <span>{{projectCategory}}</span>
            </div>
            <div class="categorySon"> 课题子类：
              <el-select v-model="projectCategorySon" @change="changeCategory" filterable allow-create
                default-first-option placeholder="请选择课题类别">
                <el-option v-for="item in projectCategorySons" :key="item.id" :label="item.name" :value="item.id">
                </el-option>
              </el-select>
            </div>
            <div class="categorySon"> 课题方向：
              <el-select v-model="projectCategorySonDirection" @change="changeCategoryDirection" filterable allow-create
                default-first-option placeholder="请选择课题方向">
                <el-option v-for="item in projectCategorySonDirections" :key="item.name" :label="item.name"
                  :value="item.name">
                </el-option>
              </el-select>
            </div>
            <!-- 课题列表 -->
            <el-table :data="projectInfos" style="width: 500px">
              <el-table-column label="分配" width="50">
                <template slot-scope="scope">
                  <el-checkbox v-model="scope.row.checked" @change="projectChecked(scope.row)"></el-checkbox>
                </template>
              </el-table-column>
              <el-table-column prop="name" label="名称" width="280"></el-table-column>
              <el-table-column prop="category_direction" label="课题方向" width="100"></el-table-column>
            </el-table>
          </div>
        </el-col>
        <el-col :span="12">
          <div>评审专家:</div>
          <el-button type="primary" @click="selectAssessor()" style="margin-top: 20px;">
            选择专家
          </el-button>
          <!-- 专家列表 -->
          <el-table :data="assessorsSelected" style="width: 500px">
            <el-table-column prop="username" label="姓名" width="280"></el-table-column>
          </el-table>
        </el-col>
      </el-row>
      <div class="distributeButton">
        <el-button type="primary" @click="distributeButton">确认分配</el-button>
      </div>
    </el-card>
    <el-card class="distributeTable">
      <el-table :data="projectDistribute" style="width: 100%">
        <el-table-column prop="pname" label="课题名称" width="580"></el-table-column>
        <el-table-column prop="aname" label="专家姓名" width="200"></el-table-column>
      </el-table>
    </el-card>
    <!-- 选择专家对话框 -->
    <el-dialog title="选择专家" :visible.sync="selectAssessorVisible">
      <div class="assessorMajors"> 专家研究方向：
        <el-select v-model="assessorMajor" @change="changeMajor" filterable allow-create default-first-option
          placeholder="请选择课题类别方向">
          <el-option v-for="item in assessorMajors" :key="item.id" :label="item.name" :value="item.id">
          </el-option>
        </el-select>
      </div>
      <!-- 专家列表 -->
      <el-table :data="assessors" style="width: 500px">
        <el-table-column label="分配" width="80">
          <template slot-scope="scope">
            <el-checkbox v-model="scope.row.checked"></el-checkbox>
          </template>
        </el-table-column>
        <el-table-column prop="username" label="姓名" width="280"></el-table-column>
      </el-table>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="assessorSelectButton()">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      projectCategory: '', //课题类别列表
      projectCategorySons: [],  //课题方向列表
      projectCategorySon: '', //选中的课题方向
      projectCategorySonDirections: [],
      projectCategorySonDirection: '',
      assessors: [],  //专家列表
      assessorMajors: ['',],  //专家研究方向列表
      assessorMajor: '', //选中的课题方向
      projectInfos: [],
      projectDistribute: [],
      selectAssessorVisible: false, //选择专家对话框
      assessorsSelected: [], //选中的专家
    }
  },
  created () {
    this.getProjectCategory()
    this.getAssessors()
    this.getAssessorMajors()
    this.getProjectDistribute()
  },
  methods: {

    //获取分配列表
    async getProjectDistribute () {
      let res = await this.axios.get('/projectDistribute/')
      if (res.status == 200) {
        this.projectDistribute = res.data.results
      } else {
        this.$message.warning('获取分配信息失败！')
      }
    },

    // 获取课题类型
    async getProjectCategory () {
      const res1 = await this.axios.get(`/projectCategory/?is_active=True`)
      if (res1.status === 200) {
        if (res1.data.results.length === 1) {
          this.projectCategory = res1.data.results[0].name
          //获取课题类别方向
          this.getProjectCategorySons()
        } else {
          this.$message.warning(`存在${res1.data.results.length}个激活类型，请联系管理员修改！`)
        }
      } else {
        this.$message.warning("获取类型错误")
      }
    },

    // 获取课题类别方向
    async getProjectCategorySons () {
      const res = await this.axios.get(`/projectCategorySon/?father_name=${this.projectCategory}`)
      if (res.status === 200) {
        this.projectCategorySons = res.data.results
        // 增加一条"所有子类"
        this.projectCategorySons.splice(0, 0, { id: 0, name: '所有子类', father_name: this.projectCategory })
        // 获取子类下的课题
        let url = 'projectInfo/?category=' + this.projectCategorySon + '&status=4'
        let resInfo = await this.axios.get(url)
        if (resInfo.status == 200) {
          this.projectInfos = resInfo.data.results
        }
      } else {
        this.$message.warning("获取方向错误")
      }
    },

    // 课题类别下拉框改变，获取课题方向列表
    async changeCategory (event) {
      if (event == 0) {
        // 选择所有子类
        let url = 'projectInfo/?status=4'
        let resInfo = await this.axios.get(url)
        if (resInfo.status == 200) {
          this.projectInfos = resInfo.data.results
        }
        return
      }
      let res = await this.axios.get('projectCategorySon/?id=' + event)
      if (res.status == 200) {
        this.projectCategorySonDirections = res.data.results[0].direction.data
        console.log(this.projectCategorySonDirections)
      }
      let url = 'projectInfo/?category=' + this.projectCategorySon + '&status=4'
      let resInfo = await this.axios.get(url)
      if (resInfo.status == 200) {
        this.projectInfos = resInfo.data.results
      }
    },

    // 课题方向下拉框改变，获取课题列表
    async changeCategoryDirection (event) {
      let url = 'projectInfo/?category=' + this.projectCategorySon +
        '&category_direction=' + this.projectCategorySonDirection +
        '&status=4'
      let res = await this.axios.get(url)
      if (res.status == 200) {
        this.projectInfos = res.data.results
        console.log(url)
      }
    },

    //获取专家列表
    async getAssessors () {
      let res = await this.axios.get(`/user/?role_id=3`)
      if (res.status === 200) {
        this.assessors = res.data.results
      } else {
        this.$message.warning("获取专家错误")
      }
    },

    // 选择专家按钮，点击显示选择对话框，选择专家
    selectAssessor () {
      this.selectAssessorVisible = true
    },

    // 获取专家研究方向
    async getAssessorMajors () {
      let res = await this.axios.get('/assessorMajor/')
      if (res.status == 200) {
        this.assessorMajors = res.data.results
        // 插入第一条，获取所有专家
        this.assessorMajors.splice(0, 0, { id: 0, name: '所有方向' })
      }
    },

    // 专家方向下拉框改变，获取专家列表
    async changeMajor (e) {
      //获取方向名称，查询专家表
      this.assessors = []
      let major = this.getMajorName(e)
      if (e == 0) {
        major = ''  //id=0时查询所有
      }
      let url = '/user/?role_id=3&major=' + major
      let res = await this.axios.get(url)
      if (res.status == 200) {
        this.assessors = res.data.results
      }
    },

    // 获取方向名称，因为专家表中存储的是名称不是id
    getMajorName (id) {
      let name = ''
      this.assessorMajors.forEach(a => {
        if (a.id == id) {
          name = a.name
        }
      })
      return name
    },

    projectChecked (item) {
      // console.log(item)
    },

    // 选择专家对话框确认按钮，初始化外层专家列表
    assessorSelectButton () {
      this.assessorsSelected = []
      for (let j = 0; j < this.assessors.length; j++) {
        if (this.assessors[j].checked) {
          this.assessorsSelected.push(this.assessors[j])
        }
      }
      this.selectAssessorVisible = false
    },

    // 确定按钮
    async distributeButton () {
      for (let i = 0; i < this.projectInfos.length; i++) {
        if (this.projectInfos[i].checked) {
          // 先删除
          let resGet = await this.axios.get('/projectDistribute/?pid=' + this.projectInfos[i].pid)
          if (resGet.status == 200) {
            let dataGet = resGet.data.results
            for (let k = 0; k < dataGet.length; k++) {
              let resDel = await this.axios.delete('/projectDistribute/' + dataGet[k].id)
              if (resDel.status != 204) {
                this.$message.warning('删除原数据失败，请稍后再试！')
              }
            }
          } else {
            this.$message.warning('获取数据失败，请稍后再试！')
            break
          }
          for (let j = 0; j < this.assessors.length; j++) {
            if (this.assessors[j].checked) {
              // console.log('assessor: ', this.assessors[j].username)
              let data = {
                pid: this.projectInfos[i].pid,
                pname: this.projectInfos[i].name,
                assessor: this.assessors[j].userid,
                aname: this.assessors[j].username
              }
              let res = await this.axios.post('/projectDistribute/', data)
              if (res.status != 201) {
                this.$message.warning('分配失败，请稍后再试！')
              }
            }
          }
        }
      }
      this.$message.success('分配成功！')
      this.getProjectDistribute()
    },

  }
}
</script>

<style lang='less'>
.el-breadcrumb {
  margin-bottom: 20px;
}

.categorySon {
  margin-top: 20px;
}
.assessorMajors {
  margin-top: 20px;
}
.distributeButton {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
.distributeTable {
  margin-top: 10px;
}
</style>