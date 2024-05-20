<script setup>
import Navbar from '../components/NavBar.vue'
import Hall from '../components/Hall.vue'
import Footer from '../components/Footer.vue'

import { links, hotelName, halls } from '@/constants.ts'
</script>

<template>
    <Navbar :links="links"/>
    <Hall v-for="hall in halls" :key="hall.id" :hall="hall"/>
    <Footer :hotelName="hotelName"/>
</template>