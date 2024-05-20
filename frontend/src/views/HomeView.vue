<script setup>
import Navbar from '../components/NavBar.vue'
import ShowCase from '../components/ShowCase.vue'
import AboutHotel from '../components/AboutHotel.vue'
import Features from '../components/Features.vue'
import Footer from '../components/Footer.vue'

import { links, hotelName } from '@/constants.ts'
</script>

<template>
  <header>
    <Navbar :links="links"/>
    <ShowCase />
    <AboutHotel />
    <Features />
    <Footer :hotelName="hotelName"/>
  </header>
</template>
