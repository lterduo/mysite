<template>

  <div>
    <button @click="bt1()">11111</button>
  </div>

</template>

<script>
export default {
  data () {
    return {
      status: [{ id: 1, name: '11' }, { id: 2, name: '22' }]
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
    }
  },


}

</script>

<style>
</style>