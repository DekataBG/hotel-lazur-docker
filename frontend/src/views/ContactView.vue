<script setup>
import Navbar from '../components/NavBar.vue'
import ContactForm from '../components/ContactForm.vue'
import ContactInfo from '../components/ContactInfo.vue'
import Footer from '../components/Footer.vue'
import { links, hotelName } from '@/constants.ts'
</script>

<template>
    <Navbar :links="links"/>
    <ContactForm/>
    <ContactInfo/>
    <Footer :hotelName="hotelName"/>
</template>