<template>
  <div id="app">
    <Navbar></Navbar>
    <br>
    <div id="content">
        <Cartographie></Cartographie>
        <About></About>
    </div>
  </div>
</template>

<script>

import About from "@/components/About";
import Cartographie from "@/components/cartography/Cartography";
import Navbar from "@/components/Navbar";

export default {
  name: 'App',
  components: {
    Navbar,
    About,
    Cartographie
  }
}
</script>

<style>

  #content {
    margin: 10px;
  }
</style>
