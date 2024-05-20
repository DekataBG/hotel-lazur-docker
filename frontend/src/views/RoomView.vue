<script setup>
import Navbar from '../components/NavBar.vue'
import Room from '../components/Room.vue'
import Footer from '../components/Footer.vue'

import { links, hotelName, room_types } from '@/constants.ts'

defineProps({
    roomId: String
})


</script>

<template>
    <Navbar :links="links"/>
    <Suspense>
        <Room :room="room_types[parseInt(roomId) - 1]" />

        <template #fallback>
            Loading...
        </template>
    </Suspense>
    <Footer :hotelName="hotelName"/>
</template>