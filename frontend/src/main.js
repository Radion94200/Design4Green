import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Presentation from "@/components/Presentation";
import Cartography from "@/components/cartography/Cartography";
import About from "@/assets/About";

Vue.config.productionTip = false;

Vue.use(VueRouter);

const routes = [
  {path: '/', component: Presentation},
  {path: '/map', component: Cartography},
  {path: '/about', component: About}
];

const router = new VueRouter({
  routes
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');

