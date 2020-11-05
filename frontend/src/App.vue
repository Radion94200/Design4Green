<template>
  <div id="app">
    <Navbar @onExtend="extend"></Navbar>
    <div id="content">

      <div id="app-home-title" class="title" @click="extend('app-home')">HOME</div>
      <div id="app-home" class="collapse show">
        <Presentation></Presentation>
      </div>

      <div id="app-cartography-title" class="title" @click="extend('app-cartography')">MAP</div>
      <div id="app-cartography" class="collapse">
        <Cartographie></Cartographie>
      </div>

      <div id="app-about-title" class="title" @click="extend('app-about')">ABOUT</div>
      <div id="app-about" class="collapse">
        <About></About>
      </div>
    </div>
  </div>
</template>

<script>

import Navbar from "@/components/Navbar";
import Presentation from "@/components/Presentation";
import About from "@/assets/About";
import Cartographie from "@/components/cartography/Cartography";

export default {
  name: 'App',
  components: {
    Cartographie,
    About,
    Presentation,
    Navbar,
  },
  data() {
    return {
      appHome: null,
      appCartography: null,
      appAbout: null,
    }
  },
  methods: {
    extend(id) {
      let appHome = window.$('#app-home');
      let appCartography = window.$('#app-cartography');
      let appAbout = window.$('#app-about');

      if (id === 'app-home') {
        appHome.collapse('show');
        appCartography.collapse('hide');
        appAbout.collapse('hide');

      } else if (id === 'app-cartography') {
        appHome.collapse('hide');
        appCartography.collapse('show');
        appAbout.collapse('hide');

      } else if (id === 'app-about') {
        appHome.collapse('hide');
        appCartography.collapse('hide');
        appAbout.collapse('show');

      }
    },
  }
}
</script>

<style>
  #app {

  }

  #content {
    margin: 10px;
  }

  .title {
    font-size: 48px;
    font-weight: bold;
    font-family: monospace;

    user-select: none;
    color: grey;
    transition: all 0.3s ease-in-out;
  }

  .title:hover {
    color: black;
    cursor: pointer;
  }
</style>
