import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue, BIcon, BIconArrowUp, BIconArrowDown, IconsPlugin, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Carousel3d from 'vue-carousel-3d';
import ElementUI from "element-ui";
import 'element-ui/lib/theme-chalk/index.css';


Vue.config.productionTip = false
Vue.use(BootstrapVue);
Vue.component('BIcon', BIcon)
Vue.component('BIconArrowUp', BIconArrowUp)
Vue.component('BIconArrowDown', BIconArrowDown)
Vue.use(BootstrapVueIcons)
Vue.use(IconsPlugin)
Vue.use(Carousel3d);
Vue.use(ElementUI);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
