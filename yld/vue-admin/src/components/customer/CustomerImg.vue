<template>
  <div>
    <div class="img-container">
      <!-- 图片 -->
      <div v-for="(item, index) in imgs" :key="index" class="imgs">
        <img :src="item.filename" alt="" />
      </div>
    </div>
    <!-- 分页器 -->
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="page_sizes"
        :page-size="page_size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
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
  mounted() {
    this.getImgs();
  },
  methods: {
    //   获取图片列表
    async getImgs() {
      const res = await this.axios.get(`/imgs/`);
      if (res.status === 200) {
        console.log(res);
        this.imgs = res.data.list;
        // 分页器总条数
        this.total = res.data.list.length;

        this.getList();
      } else {
        this.$message.warning("错误");
      }
    },
    // 构建分页显示图片列表
    getList() {
      this.pages = Math.ceil(this.total / this.page_size);
      console.log(this.pages);
    },
    // 分页
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.page_size = val;
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
    },
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