import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import CompositionApi from '@vue/composition-api';
import VueCookies from 'vue-cookies'



Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(CompositionApi);
Vue.use(VueCookies)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
