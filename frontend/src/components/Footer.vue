<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    hotelName: {
        type: String,
        required: true
    }
})

</script>

<template>
    <footer id="footer">
      <div class="container">
        <p>&copy; 2024 {{hotelName}}. All rights reserved.</p>
      </div>
    </footer>
  </template>
  
  <style scoped>
  /* Footer */
  #footer {
    background: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
  }
  
  #footer p {
    margin: 0;
  }
  
  </style>
  