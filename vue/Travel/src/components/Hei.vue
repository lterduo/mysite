<template>
    <div>
    <div>{{msg}}</div>
    <router-link to="/">hello</router-link>
    </div>
</template>

<script>
export default {
    name: 'Hei',
    data() {
        return {
            msg: 'hei!'
        }
    }
}
</script>

