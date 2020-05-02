let ObjectID = 0;

const state = {
  get newObjectID() {
    return ++ObjectID;
  }
};

const install = function(Vue, options) {
  if (Vue.prototype.$state === undefined) {
    Object.defineProperty(Vue.prototype, '$state', {
      value: state,
      writable: false,
      enumerable: true,
      configurable: true
    });
  }
}

export default {
  install
}