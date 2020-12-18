<template>

  <div>
    主页面，放重要通知
  </div>

</template>

<script>

export default {

  data () {
    return {
      data1: [
        { key: 1, label: '11', name: '111' },
        { key: 2, label: '22' },
        { key: 3, label: '33' }
      ],
      value1: [1]
      //  [{ key: 4, lable: '44' }]
    }
  },

  methods: {
    name (id) {
      const item = this.status.find(item => item.id == id)
      return item ? item.id : null
    },
    bt1 () {
      document.getElementById('div2').scrollIntoView()
    },

    async test () {
      let res = await this.axios.delete(`/projectMember/?pid=adminfeng1605502877993`)
      console.log(res)
    },

    // 上传
    uploadConfig (e) {
      let formData = new FormData();
      let data = JSON.stringify({
        user: "username",
        env: "dev"
      })
      formData.append('file', e.target.files[0]);
      formData.append('data', data);   // 上传文件的同时， 也可以上传其他数据
      let url = `/uploadFile/`;
      let config = {
        headers: { 'Content-Type': 'multipart/form-data' }
      };
      this.axios.post(url, formData, config).then(function (response) {
        console.log(response.data)
      })
    },

    handleChange (value, direction, movedKeys) {
      console.log(value, direction, movedKeys);
    },

    testBlur () {
    },
    testClick () {
      document.getElementById('input1').focus()
    }
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
.div1 {
  background: blue;
  height: 1000px;
  width: 100px;
}
.div2 {
  background: red;
  height: 1000px;
  width: 100px;
}

.se2 {
  width: 100px;
  height: 36px;
  position: absolute;
  z-index: 1;
  opacity: 0;
}
.se1 {
  position: absolute;
}
.se1:hover {
  cursor: pointer;
}
</style>