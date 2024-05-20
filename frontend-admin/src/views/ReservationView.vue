<script setup>
import { reactive } from 'vue'
import { mdiBed, mdiGithub } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import { useMainStore } from '@/stores/main'
import { ref } from 'vue'
import axios from 'axios'
import { computed } from 'vue'
import router from '@/router'


const reservation = ref({
  title: '',
  id: -1,
  roomID: -1,
  days: 0,
  startDate: '',
  email: '',
  name: '',
  phone: '',
})



const mainStore = useMainStore()

// const reservations = mainStore.reservations
// const rooms = mainStore.rooms
const roomTypes = mainStore.roomTypes

const selectOptions = computed(() => {
  return mainStore.roomTypes.map((type) => {
    return type.title
  })
})

const props = defineProps({
    reservationId: {
        type: String,
        default: -1
    }
})


if(props.reservationId != -1){
  try{
    reservation.value = mainStore.reservations.find((x) => {
      return x.id == props.reservationId
    })
    const room = mainStore.rooms.find((x) => {
      return x.id == reservation.value.roomID
    })
    const roomType = mainStore.roomTypes.find((x) => {
      return x.id == room.room_type_id
    })
    reservation.value.title = roomType.title
  }
  catch(e){
    console.log(e)
    router.push('/reservations')
  }
  console.log(reservation)
  console.log(reservation.value)
}



const typeID = computed(() => {
  console.log(roomTypes)
  const result = roomTypes.find((x) => {
    return x.title == reservation.value.title
  }).id
  console.log(result)
  return result
})

const submit = async () => {
  // validation?
  if (reservation.value.id == -1){
    await axios.post(`http://127.0.0.1:8000/room_types/${typeID.value}/reservations`, reservation.value)
  }
  else{
    try {
      await axios.post(`http://127.0.0.1:8000/room_types/${typeID.value}/reservations`, reservation.value)
    } catch (error) {
      router.push('/reservations')
      return
    }
    console.log(reservation.value.id)
    axios.delete(`http://127.0.0.1:8000/reservations/${reservation.value.id}`)
    // await axios.put(`http://127.0.0.1:8000/reservations/${reservation.id}`, reservation)
  }
  router.push('/reservations')
}

const reset = () => {
  location.reload()
}

</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiBed" title="Редактирайте резервация" main>
      </SectionTitleLineWithButton>
      <CardBox>
        <FormField label="Стая">
            <FormControl v-model="reservation.title" :options="selectOptions" />
        </FormField>

        <FormField label="Начална дата">
          <FormControl v-model="reservation.startDate" />
        </FormField>

        <FormField label="Имейл">
            <FormControl v-model="reservation.email" />
        </FormField>

        <FormField label="Име">
            <FormControl v-model="reservation.name" />
        </FormField>

        <FormField label="Телефон">
            <FormControl v-model="reservation.phone" />
        </FormField>
        <template #footer>
          <BaseButtons>
            <!-- <BaseButton type="submit" color="info" label="Запази"/> -->
            <BaseButton type="submit" color="info" label="Запази" @click="submit"/>
            <BaseButton type="reset" color="info" outline label="Поднови" @click="reset"/>
          </BaseButtons>
        </template>
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>
