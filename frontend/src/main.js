import Vue from 'vue'
import App from './App.vue'

import i18n from '@/tools/i18n/index.js';
import axios from '@/tools/axios.js';

Vue.config.productionTip = false

Vue.prototype.$axios = axios;

new Vue({
  i18n,
  render: h => h(App),
}).$mount('#app')
