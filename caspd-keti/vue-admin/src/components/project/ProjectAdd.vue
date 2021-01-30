<template>
  <div>
    <!-- 面包屑 -->
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
        <!-- 0116 隐藏状态信息 -->
        <!-- <el-table-column prop="status" label="状态" width="90">
          <template slot-scope="scope">
            <div>{{statusName(scope.row.status)}}</div>
          </template>
        </el-table-column> -->
        <el-table-column label="操作" width="150">
          <template slot-scope="scope">
            <!-- 申报书查看 -->
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-search" circle
              @click="showInfoForm(scope.row)">
            </el-button>
            <!-- 只有状态为1（待提交）或3（待修改）的才能点击修改按钮 -->
            <el-button size="mini" :plain="true" type="primary" icon="el-icon-edit" circle
              :disabled="(scope.row.status==1 || scope.row.status==3)?false:true" @click="showEditForm(scope.row)">
            </el-button>
            <!-- 只有状态为1（待提交）的才能删除 -->
            <el-button size="mini" :plain="true" type="danger" icon="el-icon-delete" circle
              :disabled="scope.row.status==111 ?false:true" @click="showDeleteForm(scope.row.id)">
            </el-button>
          </template>
        </el-table-column>
      </el-table>

    </el-card>
    <!-- 申报书新增 -->
    <el-card v-show="addFormVisible" id="id-el-card-add">
      <el-col>
        <div class="header-edit">新增申报书</div>
      </el-col>
      <!-- 课题类别 -->
      <el-card>
        <el-col class="el-col-addForm">
          <span> 课题类别：</span>
          <span>{{projectCategory}}</span>
          <span style="margin-left: 30px;"> 课题类别方向：</span>
          <el-select v-model="addForm.category" filterable allow-create default-first-option placeholder="请选择课题类别方向">
            <el-option v-for="item in projectCategorySon" :key="item.id" :label="item.name" :value="item.id">
            </el-option>
          </el-select>
        </el-col>
      </el-card>
      <el-card>
        <el-col class="el-col-addForm">
          <span> 课题名称：</span>
          <el-input v-model="addForm.name"></el-input>
        </el-col>
      </el-card>
      <!-- 项目主持人情况 -->
      <el-card class="el-card-leader">
        <div class="div-leader">
          <span>项目主持人情况</span>
          <el-button type="success" plain style="margin-left: 10px;" @click="showEditLeader()">修改信息</el-button>
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
      <!-- 预期成果形式 -->
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
      <!-- 课题研究计划 -->
      <el-card>
        <div>课题研究计划</div>
        <quill-editor v-model="addForm.content" :options="editorOption" class="editor"></quill-editor>
        <div>
          <el-button type="primary" style="margin-top: 20px;">生成申报书并下载</el-button>
        </div>
        <div class="div-file">
          <!-- 上传附件 -->
          <div class="div-upload">
            <input type="file" value="" class="input-upload" @change="uploadFile">
            <el-button type="primary" size="small" class="button-upload">上传附件
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
                  @click="deleteFile(scope.row)"></el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-card>
      <!-- 保存、提交按钮 -->
      <div class="div-add">
        <el-button type="primary" @click.prevent="addProject()" class="el-button-add">保存</el-button>
        <el-button type="primary" @click.prevent="submitProject()" class="el-button-add">提交审核</el-button>
      </div>
    </el-card>

    <!-- 申报书修改 -->
    <el-card v-show="editFormVisible" id="id-el-card-edit">
      <el-row>
        <el-col :span="24">
          <div class="header-edit">修改申报书</div>
        </el-col>
      </el-row>
      <!-- 审核意见 -->
      <el-card>
        <div style="margin-bottom: 10px;font-size: 16px;">审核意见</div>
        <quill-editor :disabled="true" v-model="auditInfo.info" :options="editorOptionAudit" class="editor-audit">
        </quill-editor>
      </el-card>

      <el-card>
        <el-col class="el-col-addForm">
          <span> 课题类别：</span>
          <span>{{projectCategory}}</span>
          <span style="margin-left: 30px;"> 课题类别方向：</span>
          <el-select v-model="editForm.category" filterable allow-create default-first-option placeholder="请选择课题类别方向">
            <el-option v-for="item in projectCategorySon" :key="item.id" :label="item.name" :value="item.id">
            </el-option>
          </el-select>
        </el-col>
      </el-card>
      <el-card>
        <el-col class="el-col-addForm">
          <span> 课题名称：</span>
          <el-input v-model="editForm.name"></el-input>
        </el-col>
      </el-card>
      <!-- 项目主持人情况 -->
      <el-card class="el-card-leader">
        <div class="div-leader">
          <span>项目主持人情况</span>
          <el-button type="success" plain style="margin-left: 10px;" @click="showEditLeader()">修改信息</el-button>
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
      <!-- 预期成果形式 -->
      <el-card>
        <el-row class="el-row-detail">
          <el-col :span="8"><span> 预期成果形式：</span>
            <el-input v-model="editForm.result_type"></el-input>
          </el-col>
          <el-col :span="8"><span> 字数：</span>
            <el-input v-model="editForm.total_words"></el-input>
          </el-col>
          <el-col :span="8"><span> 预计完成时间：</span>
            <el-input v-model="editForm.complete_time"></el-input>
          </el-col>
        </el-row>
      </el-card>
      <!-- 课题研究计划 -->
      <el-card>
        <div>课题研究计划</div>
        <quill-editor v-model="editContent" :options="editorOption" class="editor"></quill-editor>
        <div>
          <el-button type="primary" style="margin-top: 20px;" @click="genPdf()">生成申报书并下载</el-button>
        </div>
        <div class="div-file">
          <!-- 上传附件 -->
          <div class="div-upload">
            <input type="file" value="" class="input-upload" @change="uploadFileEdit">
            <el-button type="primary" size="small" class="button-upload">上传附件
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
      </el-card>
      <!-- 保存、提交按钮 -->
      <div class="div-add">
        <el-button type="primary" @click.prevent="editProject()" class="el-button-add">保存</el-button>
        <el-button type="primary" @click.prevent="submitEditProject()" class="el-button-add">提交审核</el-button>
      </div>
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
          <el-select :disabled="true" v-model="selectValue" @change="changeCategory" filterable allow-create
            default-first-option placeholder="请选择课题类别">
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
        <el-table :data="projectMember" border style="width:1021px;" :header-cell-style="{background:'#fafafa'}">
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
        <div class="div-file">
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
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-card>

    </el-card>

    <!-- 对话框 -->
    <!-- 编辑主持人对话框 -->
    <el-dialog title="编辑主持人信息" :visible.sync="editLeaderVisible">
      <el-form label-position="right" label-width="180px" :model="leader" :rules="leaderRules" class="demo-ruleForm">
        <el-form-item label="姓名" prop="username">
          <el-input v-model="leader.username" autocomplete="off"></el-input>
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
    quillEditor,
  },
  data () {
    return {
      editContent: '',
      pid: '',
      userid: '',
      query: '',  //查询条件
      projectInfo: [],
      projectCategorys: [],
      projectCategory: '',
      projectCategorySon: [],
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
            [{ 'direction': 'rtl' }],                         // 文本方向
            [{ size: ["small", false, "large", "huge"] }], // 字体大小
            [{ header: [1, 2, 3, 4, 5, 6, false] }], // 标题
            [{ color: [] }, { background: [] }], // 字体颜色、字体背景颜色
            [{ font: [] }], // 字体种类
            [{ align: [] }], // 对齐方式
            ["clean"], // 清除文本格式
            ["link", "image", "video"], // 链接、图片、视频
            // 表格
            [
              { table: 'TD' },
              { 'table-insert-row': 'TIR' },
              { 'table-insert-column': 'TIC' },
              { 'table-delete-row': 'TDR' },
              { 'table-delete-column': 'TDC' }
            ]
          ], //工具菜单栏配置
        },
        placeholder: '请在这里填写内容', //提示
        readyOnly: false, //是否只读
        theme: 'snow', //主题 snow/bubble
      },
      editorOptionAudit: {
        modules: {
          toolbar: [["bold", "italic", "underline", "strike"], // 加粗 斜体 下划线 删除线
          ["blockquote", "code-block"], // 引用  代码块
          [{ header: 1 }, { header: 2 }], // 1、2 级标题
          [{ list: "ordered" }, { list: "bullet" }], // 有序、无序列表
          ], //工具菜单栏配置
        },
      },  //审核意见

      leaderRules: {
        username: [{ required: true, message: '姓名不能为空', trigger: 'blur' },],
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
  },

  // computed: {
  //   // 编辑器
  //   editor () {
  //     return this.$refs.myQuillEditor.quill;
  //   }
  // },

  methods: {

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

    // 获取附件列表
    async getFileList (pid) {
      const res = await this.axios.get(`/fileList/?pid=${pid}`)
      if (res.status === 200) {
        this.fileList = res.data.results
      } else {
        this.$message.warning("获取文件列表错误")
      }
    },

    // 获取审核信息
    async getAuditInfo (pid) {
      this.auditInfo = {}
      const res = await this.axios.get(`/auditInfo/?pid=${pid}`)
      // if (res.status === 200) {
      if (res.data.results[0]) {
        this.auditInfo = res.data.results[0]
        this.auditContent = this.auditInfo.info
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
          const res = await this.axios.put(`/user/${this.leader.userid}/`, this.leader)
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

    // 获取类别名称
    categoryName (id) {
      const item = this.projectCategorySon.find(item => item.id == id)
      return item ? item.name : null
    },


    // 显示新增申报书卡片
    showAddForm () {
      this.addFormVisible = true
      this.editFormVisible = false
      this.infoFormVisible = false
      this.fileList = []
      setTimeout(() => {
        document.getElementById('id-el-card-add').scrollIntoView({ behavior: "smooth" })
      }, 200);
    },

    // 新增申报书
    async addProject () {
      // 写projectInfo
      this.addForm.leader = this.userid
      this.addForm.pid = this.pid
      this.addForm.status = 1
      const resProject = await this.axios.post(`/projectInfo/`, this.addForm)
      if (resProject.status !== 201) {
        return this.$message.error('新增申报书失败')
      }
      // 写projectMember
      for (var i = 0; i < this.projectMember.length; i++) {
        this.projectMember[i].pid = this.pid
        let res = await this.axios.post(`/projectMember/`, this.projectMember[i])
        if (res.status !== 201) {
          return this.$message.error('新增参加者失败，请稍后在“编辑申报书”中添加')
        }
      }
      this.$message.success('保存成功')
      setTimeout(() => {
        location.reload()
      }, 500);
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
      setTimeout(() => {
        document.getElementById("id-el-card-info").scrollIntoView({ behavior: "smooth" })
      }, 500);
    },

    // 显示编辑申报书卡片
    showEditForm (item) {
      this.editFormVisible = true
      this.infoFormVisible = false
      this.addFormVisible = false

      this.editForm = item
      //神坑啊，编辑器内容不能直接取值，必须通过中间变量取值
      this.editContent = item.content
      this.selectValue = this.categoryName(this.editForm.category) //将id转换成文字
      this.getProjectMember(item.pid)
      this.getFileList(item.pid)
      this.getAuditInfo(item.pid)

      setTimeout(() => {
        document.getElementById("id-el-card-edit").scrollIntoView({ behavior: "smooth" })
      }, 500);
    },

    //下拉框改变，改变editForm.category
    changeCategory (item) {
      this.editForm.category = item
    },

    // 编辑申报书，保存
    async editProject () {
      // 写projectInfo
      this.editForm.leader = this.userid
      this.editForm.status = 1
      this.editForm.content = this.editContent //quill的神坑
      const resProject = await this.axios.put(`/projectInfo/${this.editForm.id}/`, this.editForm)

      if (resProject.status !== 200) {
        return this.$message.error('编辑申报书失败')
      }
      // 写projectMember
      // 1、删除原有成员
      let resDelete = await this.axios.get(`/projectMember/?pid=${this.editForm.pid}`)
      let memberTemp = resDelete.data.results
      for (var i = 0; i < memberTemp.length; i++) {
        let res = await this.axios.delete(`/projectMember/${memberTemp[i].id}`)
      }
      // 2、新增
      for (var i = 0; i < this.projectMember.length; i++) {
        this.projectMember[i].pid = this.editForm.pid
        let res = await this.axios.post(`/projectMember/`, this.projectMember[i])
        if (res.status !== 201) {
          return this.$message.error('新增参加者失败，请稍后再试')
        }
      }
      this.$message.success('保存成功')
      setTimeout(() => {
        location.reload()
      }, 500);
    },

    // 编辑申报书，提交
    async submitEditProject () {
      // 写projectInfo
      this.editForm.leader = this.userid
      this.editForm.status = 2
      this.editForm.content = this.editContent
      const resProject = await this.axios.put(`/projectInfo/${this.editForm.id}/`, this.editForm)

      if (resProject.status !== 200) {
        return this.$message.error('编辑申报书失败')
      }
      // 写projectMember
      // 1、删除原有成员
      let resDelete = await this.axios.get(`/projectMember/?pid=${this.editForm.pid}`)
      let memberTemp = resDelete.data.results
      for (var i = 0; i < memberTemp.length; i++) {
        let res = await this.axios.delete(`/projectMember/${memberTemp[i].id}`)
      }
      // 2、新增
      for (var i = 0; i < this.projectMember.length; i++) {
        this.projectMember[i].pid = this.editForm.pid
        let res = await this.axios.post(`/projectMember/`, this.projectMember[i])
        if (res.status !== 201) {
          return this.$message.error('新增参加者失败，请稍后再试')
        }
      }
      this.$message.success('保存成功')
      setTimeout(() => {
        location.reload()
      }, 500);
    },

    // 生成申报书并下载
    async genPdf () {
      // console.log(this.editContent)
      let data = { 'content': this.editContent }
      let res = await this.axios.post('/genPdf/', this.editContent)
      console.log(res)
    },

    // 上传文件，新增申报书
    uploadFile (e) {
      let formData = new FormData();
      let data = JSON.stringify({
        pid: this.pid
      })
      formData.append('file', e.target.files[0]);
      formData.append('data', data);   // 上传文件的同时， 也可以上传其他数据
      let url = `/uploadFile/`;
      let config = {
        headers: { 'Content-Type': 'multipart/form-data' }
      };
      this.axios.post(url, formData, config).then((response) => {
        this.getFileList(this.pid)
      })
    },


    // 上传，编辑申报书，pid存在
    uploadFileEdit (e) {
      let formData = new FormData();
      let data = JSON.stringify({
        pid: this.editForm.pid
      })
      formData.append('file', e.target.files[0]);
      formData.append('data', data);   // 上传文件的同时， 也可以上传其他数据
      let url = `/uploadFile/`;
      let config = {
        headers: { 'Content-Type': 'multipart/form-data' }
      };
      this.axios.post(url, formData, config).then((response) => {
        console.log(response.data)
        this.getFileList(this.editForm.pid)
        console.log('fileList:  ', this.fileList)
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
      console.log(resDelete)
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

    test () {
      console.log('test:  ', this.editForm.content)
      document.getElementById("test").scrollIntoView()
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
  .ql-editor {
    min-height: 200px;
  }
}
.editor-audit {
  .ql-editor {
    min-height: 100px;
  }
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
</style>