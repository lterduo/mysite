<template>
  <div>
    <!-- 面包屑 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>
        <a>客户信息维护</a>
      </el-breadcrumb-item>
      <el-breadcrumb-item>客户头像筛选</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="img-container">
      <!-- 图片 -->
      <div v-for="(item, index) in listPagination" :key="index" class="imgs">
        <img :src="item.filename" alt="" @click="imgClick(item.filename)" />
      </div>
    </div>
    <!-- 分页器 -->
    <div class="block">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage"
        :page-sizes="page_sizes" :page-size="page_size" layout="total, sizes, prev, pager, next, jumper" :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      imgs: [],
      //分页
      currentPage: 1,
      page_size: 20,
      page_sizes: [20, 30, 40, 50],
      total: 0,
      //   分页显示的图片
      pages: 0,
      listPagination: [],
    };
  },
  mounted () {
    this.getImgs();
  },
  methods: {
    //   获取图片列表
    async getImgs () {
      const res = await this.axios.get(`/unprocessed/`);
      if (res.status === 200) {
        this.imgs = res.data.list;
        // 分页器总条数
        this.total = res.data.list.length;

        this.getList();
      } else {
        this.$message.warning("错误");
      }
    },
    // 构建分页显示图片列表
    getList () {
      // 总页数，向上取整
      this.pages = Math.ceil(this.total / this.page_size);
      // 将imgs按页数分割，listPagination按照currentPage赋值
      this.listPagination = []
      for (let i = 0; i < this.page_size; i++) {
        // j 为imgs的索引
        let j = i + (this.page_size * (this.currentPage - 1))
        if (j < this.total) {
          this.listPagination[i] = this.imgs[i + (this.page_size * (this.currentPage - 1))]
        }
      }
    },
    // 分页
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`);
      this.page_size = val;
      this.getList()
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
      this.getList()
    },

    // 点击图片，跳转
    imgClick (filename) {
      this.$router.push({ name: 'customerAdd', params: { filename: filename } })
    }
  },
};
</script>

<style lang='less'>
.img-container {
  display: flex;
  flex-wrap: wrap;
  .imgs {
    padding: 2px;
    border: 2px solid black;
  }
}
</style>