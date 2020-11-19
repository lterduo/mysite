<template>
  <el-container class="container">
    <!-- 头部：logo、系统名称、头像退出 -->
    <el-header class="header">
      <el-row>
        <el-col :span="4" class="logo">
          <img src="../../assets/image/logo.png" alt="" />
        </el-col>
        <el-col :span="16" class="sys-name"> 课题申报系统 </el-col>
        <el-col class="logout" :span="4">
          <div>
            <a class="el-icon-user" @click="userInfo()"></a>
            <a @click.prevent="logout()" href="#">退出</a>
          </div>
        </el-col>
      </el-row>
    </el-header>

    <el-container>
      <!-- 侧边栏导航 -->
      <el-aside class="aside" width="240px">
        <el-menu :unique-opened="true" :router="true" background-color="#545c64" text-color="#fff">
          <!-- 1 -->
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>申报人管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="applicant">申报人管理</el-menu-item>
          </el-submenu>
          <!-- 2 -->
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>专家管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="expert">专家管理</el-menu-item>
          </el-submenu>
          <!-- 3 -->
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>课题类别管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="projectCategory">课题类别</el-menu-item>
          </el-submenu>
          <!-- 4 -->
          <el-submenu index="4">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>申报书管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="projectAdd">申报书填写</el-menu-item>
            <el-menu-item class="el-icon-s-unfold" index="projectAudit">申报书审核</el-menu-item>
          </el-submenu>
          <!-- 5 -->
          <el-submenu index="5">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>申报书分配</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="projectDistribute">申报书分配</el-menu-item>
          </el-submenu>
          <!-- 5 -->
          <el-submenu index="5">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>立项评审</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="projectAssess">申报书评审</el-menu-item>
          </el-submenu>
          <!-- 6 -->
          <el-submenu index="6">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>系统管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="1-2">选项2</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 内容区 -->
      <el-main class="main">
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  beforeCreate () {
    //获取token
    const token = localStorage.getItem("token")
    //如果没有，跳转登录
    if (!token) {
      this.$router.push({ name: "login" })
    }
    //如果有，继续渲染
  },
  methods: {
    logout () {
      //清除token
      localStorage.clear()
      this.$message.success("退出成功")
      this.$router.push({ name: "login" })
    },
    userInfo () {
      alert('hei')
    }
  },
} 
</script >

<style scoped lang="less">
.container {
  height: 100%;

  .header {
    margin: 0;
    padding: 0;
    background-color: #fff;
    font-size: 24px;
    border-bottom: 1px solid #e6e6e6;

    .logo {
      display: flex;
      padding-left: 10px;
      img {
        height: 59px;
      }
    }
    .sys-name {
      text-align: center;
      line-height: 60px;
    }
    .logout {
      display: flex;
      justify-content: flex-end;
      padding-right: 10px;
      font-size: 14px;
      align-items: center;
      height: 60px;
      a {
        text-decoration: none;
        font-size: 16px;
        color: #000;
        margin-right: 10px;
      }
      .el-icon-user {
        font-size: 25px;
      }
      a:hover {
        cursor: pointer;
      }
    }
  }
}
.aside {
  background-color: #545c64;
}
.main {
  background-color: #fff;
}
</style>