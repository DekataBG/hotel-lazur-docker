<script setup>
import Navbar from '../components/NavBar.vue'
import Reservation from '../components/Reservation.vue'
import Footer from '../components/Footer.vue'

import { links, hotelName, halls } from '@/constants.ts'
</script>

<template>
    <Navbar :links="links"/>
    <Reservation/>
    <Footer :hotelName="hotelName"/>
</template>