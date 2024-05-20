<script setup>
import { computed, ref } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiPencil, mdiTrashCan } from '@mdi/js'
import CardBoxModal from '@/components/CardBoxModal.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import router from '@/router'
import CardBoxModalReservationDelete from './CardBoxModalReservationDelete.vue'

defineProps({
  checkable: Boolean
})

const mainStore = useMainStore()

const items = computed(() => mainStore.reservations)

console.log(items)

const isModalDangerActive = ref({
  active: false,
  id: -1,
})

const perPage = ref(10)

const currentPage = ref(0)

const itemsPaginated = computed(() =>
  items.value.slice(perPage.value * currentPage.value, perPage.value * (currentPage.value + 1))
)

const numPages = computed(() => Math.ceil(items.value.length / perPage.value))

const currentPageHuman = computed(() => currentPage.value + 1)

const pagesList = computed(() => {
  const pagesList = []

  for (let i = 0; i < numPages.value; i++) {
    pagesList.push(i)
  }

  return pagesList
})

function redirect(reservationID) {
  router.push({ path: `/reservations/${reservationID}`})
}

const deleteReservation = (room_id) => {
  for (let i = 0; i < mainStore.reservations.length; i++) {
    if(room_id == mainStore.reservations[i].id){
      mainStore.reservations.splice(i, 1)
      break
    }
  }
  console.log(mainStore.reservations)
}

</script>

<template>
  <CardBoxModalReservationDelete @confirm="deleteReservation" v-model="isModalDangerActive" title="Потвърдете" button="danger" button-label="Изтрий" has-cancel />

  <table>
    <thead>
      <tr>
        <th>Стая</th>
        <th>Начална дата</th>
        <th>Дни престой</th>
        <th>Имейл</th>
        <th>Име</th>
        <th>Телефонен номер</th>
        <th/>
      </tr>
    </thead>
    <tbody>
      <tr v-for="reservation in itemsPaginated" :key="reservation.id">
        <td data-label="Room">
          {{ reservation.roomID }}
        </td>
        <td data-label="Startdate">
          {{ reservation.startDate }}
        </td>
        <td data-label="Days">
            {{ reservation.days }}
        </td>
        <td data-label="Email">
            {{ reservation.email }}
        </td>
        <td data-label="Name">
            {{ reservation.name }}
        </td>
        <td data-label="Phone">
            {{ reservation.phone }}
        </td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiPencil" small @click="redirect(reservation.id)" />
            <BaseButton
              color="danger"
              :icon="mdiTrashCan"
              small
              @click="() => {
                isModalDangerActive.active = true
                isModalDangerActive.id = reservation.id
              }"
            />
          </BaseButtons>
        </td>
      </tr>
    </tbody>
   </table>
  <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
    <BaseLevel>
      <BaseButtons>
        <BaseButton
          v-for="page in pagesList"
          :key="page"
          :active="page === currentPage"
          :label="page + 1"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'"
          small
          @click="currentPage = page"
        />
      </BaseButtons>
      <small>Страница {{ currentPageHuman }} от {{ numPages }}</small>
    </BaseLevel>
  </div>
</template>
