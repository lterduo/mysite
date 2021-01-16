<template>
  <div>
    <div>
      <vue-wangeditor v-model="text"></vue-wangeditor>
    </div>
  </div>

</template>

<script>
import vueWangeditor from 'vue-wangeditor'

export default {
  components: { vueWangeditor, },
  data () {
    return {
      text: '',
      disabledMenus: ''
    }
  },

  methods: {

  }
}

</script>

<style lang="less" >
</style>