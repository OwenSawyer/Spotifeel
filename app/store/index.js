import Vuex from 'vuex'
import Vue from 'vue'
import cart from './cart'
import products from './products'
import test from './test'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    cart,
    products,
    test
  }
})
