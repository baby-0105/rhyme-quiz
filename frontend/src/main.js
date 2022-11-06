import 'bootstrap/dist/css/bootstrap.css';
import '@/assets/style/tailwind-input.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
import { createApp } from 'vue';

import App from './App.vue';
import router from './router';


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8888/';

const app = createApp(App)
app.use(router).use(VueAxios, axios).mount('#app')
