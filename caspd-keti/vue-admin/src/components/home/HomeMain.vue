<template>
  <div>
    <div>
      <!-- ueditor
      <vue-ueditor-wrap v-model="text" :config="editorConfig"></vue-ueditor-wrap> -->
    </div>
  </div>

</template>

<script>
// import VueUeditorWrap from 'vue-ueditor-wrap'

export default {
  // components: {
  //   VueUeditorWrap
  // },
  data () {
    return {
      text: '',
      // editorConfig: {
      //   autoHeightEnabled: false, //编译器不自动被内容撑高
      //   initialFrameHeight: 350, //初始容器高度
      //   initialFrameWith: 900,
      //   // serverUrl: "/api/ueditor/net/controller.ashx", //上传文件地址
      //   UEDITOR_HOME_URL: "/static/UEditor/", //UEditor资源文件的存放路径
      // },
    }
  },

  methods: {

  }
}

</script>

<style lang="less" >
</style>