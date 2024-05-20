<script lang='ts' setup>
import { defineProps, ref, onMounted, computed, defineComponent } from 'vue';
import { addDays, subDays } from 'date-fns';
import ServicesIcons from '../components/ServicesIcons.vue'
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import { addReservation, fetchReservationsForType, fetchRoomsFromType } from '@/plugins/api';
import { useToast } from 'vue-toast-notification';
import { AxiosError } from 'axios';
import type { DatePickerInstance } from "@vuepic/vue-datepicker"

import { mapMutations } from '../vuex-helper.js'

const { addItem } = mapMutations()

const props = defineProps({
  room: {
    type: Object,
    required: true,
  },
});


const parts = props.room.imagePath.split('/')
const fileName = parts[parts.length - 1]
const roomTypeReservations = await fetchReservationsForType(props.room.id);
const $toast = useToast();

const date = ref();
const datepicker = ref<DatePickerInstance>(null);
const disabledDates = roomTypeReservations.map( (x) => {
  let dates = []
  const [year, month, day] = x.startDate.split('-').map(Number);
  let xDate = new Date(year, month - 1, day)
  while (x.days > 0){
    dates.push(xDate); // YYYY-MM-DD
    x.days--;
    xDate = subDays(xDate, 1)
  }
  return getPassedDatesInYear().concat(dates)
}).flat();

function getPassedDatesInYear(): Date[] {
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const passedDates: Date[] = [];

    for (let month = 0; month < currentDate.getMonth() + 1; month++) {
        const daysInMonth = new Date(currentYear, month + 1, 0).getDate();
        const lastDayOfMonth = month === currentDate.getMonth() ? currentDate.getDate() : daysInMonth;

        for (let day = 1; day <= lastDayOfMonth; day++) {
            const date = new Date(currentYear, month, day);
            passedDates.push(date);
        }
    }

    return passedDates;
}

const nameText = ref('')
const emailText = ref('')
const phoneText = ref('')

function addToCart(item) {
  if(!(date.value && date.value[0] && date.value[1])) {
    $toast.open({
      message: 'Изберете дати за престой.',
      type: 'error',
      position: 'top'
    });

    return;
  }

  $toast.open({
      message: 'Стаята е добавена в количката',
      type: 'success',
      position: 'top'
  });

  item.date = date.value;
  console.log(item.date)
  addItem(item);
  
  datepicker.value!.clearValue();
}
</script>

<template>
  <h1 class="title text-center mt-3">{{ room.title }}</h1>
  <div class="text-center mb-5">
    <img
      :src="`/rooms/${fileName}`"
      :alt="room.title"
      class="room-img"
    />
  </div>
  <div class="row justify-content-center">
    <div class="col-12 col-md-8">
      <p class="text-center description">{{room.features}}</p>
      <div class="divider mt-4 mb-4"></div>
    </div>
  </div>
  <div class="text-center fw-bold mb-3">
      <h5 class="mb-4">Характеристики</h5>
      <div style="--font-size: 30px; --margin-size: 10px;">
        <ServicesIcons />
      </div>
  </div>
  <div class="row justify-content-center">
    <div class="col-12 col-md-8">
      <div class="divider mt-4 mb-4"></div>
    </div>
  </div>
  <div class="text-center fw-bold">
    <h3 class="primary-text">РЕЗЕРВИРАЙ СЕГА</h3>
  </div>
  <div class="booking row justify-content-center mb-3 p-4">
    <div class="col-3">
      <VueDatePicker 
        v-model="date"
        placeholder="Избери дати"
        :range="{ noDisabledRange: true }"
        :disabled-dates="disabledDates"
        locale="bg"
        format="P"
        ref="datepicker"
      />
</div>
    <div class="col-2">
        <button class="booking-button" @click="addToCart(room)">Добави в количка</button>
    </div>
  </div>
  <div class="modal fade" id="SubmitPersonalInfoModal" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Лична информация</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="name" class="form-label">Име</label>
              <input v-model="nameText" type="text" name="Name" id="Name" class="form-control">
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Имейл</label>
              <input v-model="emailText" type="email" name="email" id="email" class="form-control">
            </div>
            <div class="mb-3">
              <label for="phone" class="form-label">Телефонен номер</label>
              <input v-model="phoneText" type="text" name="phone" id="phone" class="form-control">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Затвори</button>
          <button type="button" class="btn btn-primary" @click="sendReservation()">Резервирай</button>
        </div>
      </div>
    </div>
  
  </div>
</template>

<style scoped>
.title, .description {
  color: #033f59;
}

.room-img {
  width: 110vh;
  height: 65vh;
  border-radius: 5%;
  border-width: 2px;
  border-style: solid;
}

.divider {
    border-top: 0.5px solid black;
}

p {
    font-size: 17px;
}

.booking {
    background-color: #eee;
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
