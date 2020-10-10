<template>
  <el-container class="container">
    <el-header class="header">
      <el-row :gutter="20">
        <el-col :span="4">
          <div class="grid-content bg-purple">
            <h2>图标</h2>
          </div>
        </el-col>
        <el-col :span="16">
          <div class="grid-content bg-purple-light">
            <h2>后台管理</h2>
          </div>
        </el-col>
        <el-col class="logout" :span="4">
          <div class="grid-content bg-purple">
            <a @click.prevent="logout()" href="#">退出</a>
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <el-aside class="aside" width="200px">
        <!-- 侧边栏导航 -->
        <el-menu :unique-opened="true" :router="true">
          <!-- 1 -->
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>用户管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="users">用户列表</el-menu-item>
          </el-submenu>
          <!-- 2 -->
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>权限管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="1-2">角色列表</el-menu-item>
            <el-menu-item class="el-icon-s-unfold" index="1-2">权限列表</el-menu-item>
          </el-submenu>
          <!-- 3 -->
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>商品管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="1-2">商品列表</el-menu-item>
            <el-menu-item class="el-icon-s-unfold" index="1-2">分类列表</el-menu-item>
            <el-menu-item class="el-icon-s-unfold" index="1-2">商品列表</el-menu-item>
          </el-submenu>
          <!-- 4 -->
          <el-submenu index="4">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>订单管理</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="1-2">选项2</el-menu-item>
          </el-submenu>
          <!-- 5 -->
          <el-submenu index="5">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>查询统计</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" index="1-2">选项2</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main class="main">
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  beforeCreate() {
    //获取token
    const token = localStorage.getItem("token");
    //如果没有，跳转登录
    if (!token) {
      this.$router.push({ name: "login" });
    }
    //如果有，继续渲染
  },
  methods: {
    logout() {
      //清除token
      localStorage.clear();
      this.$message.success("退出成功");
      this.$router.push({ name: "login" });
    },
  },
};
</script>

<style>
.container {
  height: 100%;
}
.header {
  background-color: #b3c0d1;
}
.aside {
  background-color: #d3dce6;
}
.main {
  background-color: #fff;
}
.logout {
  line-height: 56px;
}

.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>