<script setup>
import Navbar from '../components/NavBar.vue'
import Rooms from '../components/Rooms.vue'
import Footer from '../components/Footer.vue'

import { links, hotelName, room_types } from '@/constants.ts'
</script>

<template>
    <Navbar :links="links"/>
    <Rooms :rooms="room_types" />
    <Footer :hotelName="hotelName"/>
</template>