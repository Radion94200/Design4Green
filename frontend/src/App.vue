<template>
  <div id="app">
    <Navbar></Navbar>
    <div id="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

import Navbar from "@/components/Navbar";

export default {
  name: 'App',
  components: {
    Navbar,
  }
}
</script>

<style>
  #app {

  }
  #content {
    margin: 15px
  }

  .p {

  }
</style>
