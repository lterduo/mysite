<template>

  <div>
    <button @click="bt1()">11111</button>
    <el-card>
      <el-col>
        <div class="header-edit">新增申报书</div>
      </el-col>
      <el-col class="tab-col">
        <div>类别：</div>
        <el-input></el-input>
        <div>名称：</div>
        <el-input v-model="addForm.name"></el-input>
      </el-col>
    </el-card>

    <el-table :data="tableData" style="width: 100%" border>
      <el-table-column prop="bookname" :label="recoveryOne" width="140px">
        <template slot-scope="scope">
          <el-input v-model="scope.row.bookname" type="number"></el-input>
        </template>
      </el-table-column>

      <el-table-column prop="bookvolume" :label="recoveryTwo" width="140px">
        <template slot-scope="scope">
          <el-input v-model="scope.row.bookvolume" type="number"></el-input>
        </template>
      </el-table-column>

      <el-table-column prop="bookborrower" :label="recoveryThree" width="150px">
        <template slot-scope="scope">
          <el-input v-model="scope.row.bookborrower" type="number"></el-input>
        </template>
      </el-table-column>

      <el-table-column>
        <template slot-scope="scope">
          <button @click="addLine" class="addBtn" v-if="scope.$index == tableData.length - 1">
            <i class="el-icon-plus"></i>
          </button>

          <button v-if="tableData.length > 1" @click="handleDelete(scope.$index, scope.row)" class="del-btn">
            <i class="el-icon-minus"></i>
          </button>
        </template>
      </el-table-column>
    </el-table>
  </div>

</template>

<script>
export default {
  data () {
    return {
      status: [{ id: 1, name: '11' }, { id: 2, name: '22' }],
      addForm: {},
      tableData: [{
        bookname: '',
        bookborrower: '',
        bookvolume: ''
      },],
    };
  },
  methods: {
    name (id) {
      // var name = ''
      // this.status.forEach((s) => {
      //   console.log(s.id)
      //   console.log(s.name)
      //   if (s.id == id) {
      //     console.log(s.id, '   ', s.name)
      //     name = s.name
      //   }
      // })
      // return name
      const item = this.status.find(item => item.id == id)
      return item ? item.id : null
    },
    bt1 () {
      var t = this.name(4)
      console.log('return:  ', t)
    },

    addLine () { //添加行数
      var newValue = {
        bookname: '',
        bookborrower: '',
        bookvolume: ''
      };
      //添加新的行数
      this.tableData.push(newValue);
    },
    handleDelete (index) { //删除行数
      this.tableData.splice(index, 1)
    },
  },


}

</script>

<style lang="less" scoped>
.tab-col {
  display: flex;
  justify-content: flex-start;
  div {
    display: flex;
    align-items: center;
  }
  .el-input {
    width: 300px;
    margin-left: 5px;
    margin-right: 10px;
  }
}
</style>