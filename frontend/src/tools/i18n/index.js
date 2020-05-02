import Vue from 'vue';
import VueI18n from 'vue-i18n';
import ru from './languages/ru.json';

let locale = 'ru';
Vue.use(VueI18n);

const vueI18n = new VueI18n({
  locale,
  messages: {
    ru
  }
});

export default vueI18n;
