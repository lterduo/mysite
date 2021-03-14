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
          <el-submenu v-for="item in menus.data" :key="item.id" :index="item.id.toString()">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{item.name}}</span>
            </template>
            <el-menu-item class="el-icon-s-unfold" :index="itemSub.path" v-for="itemSub in item.children"
              :key="itemSub.id">
              {{itemSub.name}}
            </el-menu-item>
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
  data () {
    return {
      menus: {}

    }
  },
  created () {
    //获取token
    // const token = localStorage.getItem("token")
    // 获取菜单
    const menus = localStorage.getItem("menus")
    this.menus = JSON.parse(menus)

    //如果没有，跳转登录
    // if (!token) {
    //   this.$router.push({ name: "login" })
    // }
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

<style  lang="less">
.container {
  height: 100%;

  .header {
    margin: 0;
    padding: 0;
    background-color: #fff;
    font-size: 24px;
    border-bottom: 1px solid #e6e6e6;

    .el-row {
      width: 100%;
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
        align-items: center;
        padding-right: 10px;
        font-size: 14px;
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
}
.aside {
  background-color: #545c64;
}
.main {
  background-color: #fff;
  height: 100%;
}
</style>