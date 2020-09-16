<template>
  <div id="app">
    <app-nav></app-nav>
    <div class="pg-body">
      <app-slider></app-slider>
      <div class="content">
          <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import appNav from "./components/common/appnav.vue";
import appSlider from "./components/common/appslider";
import list from "./components/list/list.vue";
import details from "./components/details/details.vue";
import bar from './components/bar/bar'

export default {
  name: "app",
  components: {
    appNav: appNav,
    appSlider,
    list,
    details,
  },
  data() {
    return {};
  },
};
</script>

<style>
</style>
