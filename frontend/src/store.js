// Vuex store definition
import { createStore } from 'vuex';

const store = createStore({
  state: {
    cartItems: []
  },
  getters: {
    getCartItems: state => {
      return state.cartItems;
    },
    getCartItemsCount: state => {
      return state.cartItems.length;
    }
  },
  mutations: {
    addItem(state, item) {
        state.cartItems.push(item);
    },
    removeItem(state, itemToRemove) {
        state.cartItems = state.cartItems.filter(item => item.id != itemToRemove.id)
    },
    clearItems(state) {
      state.cartItems = []
    }
  },
  actions: {
    // Define your actions here
  }
});

export default store;
