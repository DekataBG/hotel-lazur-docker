<script setup lang="ts">
import { mapGetters, mapMutations } from '../vuex-helper.js'
import { ref } from 'vue';
import { useToast } from 'vue-toast-notification';
import { addReservation } from '@/plugins/api';
import { AxiosError } from 'axios';
import ModalComponent from "./ModalComponent.vue";

const $toast = useToast();

const { getCartItems, getCartItemsCount } = mapGetters()
const { clearItems, removeItem } = mapMutations()

async function sendReservation (email, name, phoneNumber) {
  for(const room of getCartItems.value) {
    if(room.date && room.date[0] && room.date[1]){
        const dateStart = `${room.date[0].getFullYear()}-${('0' + (room.date[0].getMonth() + 1)).slice(-2)}-${('0' + room.date[0].getDate()).slice(-2)}`;

        const days = Math.floor((room.date[1].getTime() - room.date[0].getTime()) / (1000 * 60 * 60 * 24)) + 1

        const result = await addReservation(room.id, dateStart, days, email, name, phoneNumber)
        console.log(result)
        if(result instanceof AxiosError){
            console.error(result)
            $toast.open({
                message: 'Error! ' + result.response!.status + ' ' + result.response!.statusText,
                type: 'error',
                position: 'top'
            });
            return;
        }
    }
  }
    $toast.open({
        message: 'Направена е резервация',
        type: 'success',
        position: 'top'
    });

    clearItems();
    isModalOpened.value = false
}

function calculatePrice(room) {
    const days = Math.floor((room.date[1].getTime() - room.date[0].getTime()) / (1000 * 60 * 60 * 24)) + 1
    const price = room.price

    return days * price
}

const isModalOpened = ref(false);

const openModal = () => {
  isModalOpened.value = true;
};
const closeModal = () => {
  isModalOpened.value = false;
};

const submitHandler = async (person) => {
    if(person.name === null || person.name === undefined || person.name.trim() === '') {
    $toast.open({
      message: 'Въведете име',
      type: 'error',
      position: 'top'
    });
    return
  }

  const emailRegex: RegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if(!emailRegex.test(person.email)) {
    $toast.open({
      message: 'Невалиден имейл',
      type: 'error',
      position: 'top'
    });
    return
  }

  const phoneRegex: RegExp = /^(\+)?\d+$/;
    if(!phoneRegex.test(person.phoneNumber)) {
    $toast.open({
      message: 'Невалиден телефонен номер',
      type: 'error',
      position: 'top'
    });
    return
  }
  await sendReservation(person.email, person.name, person.phoneNumber)
}
</script>

<template>
      <ModalComponent :isOpen="isModalOpened" @modal-close="closeModal" @submit="submitHandler" name="first-modal">
      </ModalComponent>
      
    <section v-if="getCartItemsCount > 0" id="about-info" class="py-3">
        <div class="container mb-3" v-for="item in getCartItems">
            <div class="info-left">
                <h1 class="l-heading"> {{ item.title }} </h1>
                <p>{{ calculatePrice(item) }} лв.</p>
            </div>
            <div class="info-right">
                <img :src="`/rooms/${item.imagePath}`" :alt="СнимкаНаСтаята">
                <div class="close">
                    <i class="fas fa-times-circle vbo-icn-carat vbo-pref-color-text" @click="removeItem(item)"></i>
                </div>
            </div>
        </div>

        <div class="text-center mt-5">
            <button class="booking-button" @click="openModal">РЕЗЕРВИРАЙ</button>
        </div>
    </section>
    <section v-if="getCartItemsCount == 0" id="about-info" class="py-3">
        <h1 class="text-center">Количката е празна</h1>
    </section>
</template>

<style scoped>
.container:hover {
    background-color: #f7f8f3;
}

/* About Info */
#about-info .info-right{
    float:right;
    width:50%;
    min-height:100%;
}
#about-info .info-left{
    float:left;
    width:50%;
    min-height: 100%;
}

#about-info .info-right img{
    display:block;
    margin:auto;

    border-radius: 20%;
}

img {
    height: 25vh;
    width: 40vh;
    border-style: solid;
    border-width: 1px;
}

.container {
    border-bottom-style: solid;
    border-bottom-width: 0.2px;
    border-bottom-color: rgb(156, 156, 160);
    position: relative;
}

.close {
    float: right;
    position: absolute;
    top: 0;
    right: 0;
    margin-top: 5px;
    margin-right: 5px;
}

.booking-button {
	background: #cb5951;
	border-radius:30px;
	color: #fff;
	padding: 10px;
}

.booking-button:hover {
	color: #fff;
	background: #4B7B92;
}
</style>