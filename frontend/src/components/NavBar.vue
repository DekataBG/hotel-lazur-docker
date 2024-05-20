<script setup>
import { defineProps } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { mapGetters } from '../vuex-helper.js'

const { getCartItemsCount } = mapGetters()

const props = defineProps({
    links: {
        type: Array,
        required: true
    }
})

const route = useRoute()
const currentPath = route.path
</script>

<template>
    <nav id="navbar">
        <div class="container">  
            <RouterLink to="/">
                <img class="logoimage" src="../assets/img/logo.png" alt="Samanta">
            </RouterLink>
            <ul>
                <RouterLink 
                    :to="link.path"
                    v-for="link in links"
                    :key="link.id"
                >
                    <li>
                        <a :class="currentPath == link.path ? 'current' : '!current'">{{link.title}}</a>
                    </li>
                </RouterLink>
                <RouterLink to="/cart">
                    <div class="cart-container">
                        <button class="cart-button">
                            <i class="fa fa-shopping-cart fa-2x mt-4 ms-5" id="cart"></i>
                        </button>
                        <div class="cart-badge" v-if="getCartItemsCount > 0">
                            {{ getCartItemsCount }}
                        </div>
                      </div>
                </RouterLink>
            </ul>
        </div>
    </nav>  
</template>

<style>
/* Navbar */
#navbar{
    background:#333;
    color:#fff;
    overflow:auto;
}

#navbar a{
    color:#fff
}

#navbar ul{
    list-style:none;
    float:right;
}

#navbar ul li {
 float:left;
}

#navbar ul li a{
    display:block;
    padding:20px;
    text-align: center;
}

#navbar ul li a:hover,
 #navbar ul li a.current{
    background:#444;
    color:#f7c08a;
}

.logoimage {
    width: 17vh;
    height: 9vh;
}

#cart:hover {
    color: #f7c08a;
}

#cart {
    color: white;
}

.cart-container {
  position: relative;
  display: inline-block;
}

.cart-button {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
}

.cart-badge {
  position: absolute;
  top: 5px;
  right: -15px;
  background-color: white;
  color: black;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12px;
}
</style>
