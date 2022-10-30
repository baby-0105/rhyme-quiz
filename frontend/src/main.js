import 'bootstrap/dist/css/bootstrap.css';
import '@/assets/style/tailwind-input.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vue from 'vue';

import App from './App.vue';
import router from './router';


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8888/';

Vue.config.productionTip = false;

Vue.use(VueAxios, axios)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
