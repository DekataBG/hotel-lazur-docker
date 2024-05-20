<script setup>
import Navbar from '../components/NavBar.vue'
import About from '../components/About.vue'
import Footer from '../components/Footer.vue'
import Guests from '../components/Guests.vue'

import { links, hotelName } from '@/constants.ts'
</script>

<template>
    <Navbar :links="links"/>
    <About/>
    <Guests />
    <Footer :hotelName="hotelName"/>
</template>