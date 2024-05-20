<script setup>
import { computed, ref } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiPencil, mdiTrashCan } from '@mdi/js'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import CardBoxModalRoomDelete from './CardBoxModalRoomDelete.vue'
import router from '@/router'

defineProps({
  checkable: Boolean
})

const mainStore = useMainStore()

const items = computed(() => mainStore.roomTypes)

const isModalDangerActive = ref({
  active: false,
  id: -1
})

const perPage = ref(10)

const currentPage = ref(0)

const itemsPaginated = computed(() =>
  items
    .value
    .slice(perPage.value * currentPage.value, perPage.value * (currentPage.value + 1))
    .map((item) => {
      let shortDescription = item.description
      if(shortDescription.length > 30){
        shortDescription = item.description.slice(0, 30) + '...'
      }

      return {
        title: item.title,
        description: item.description,
        features: item.features,
        id: item.id,
        imagePath: item.imagePath,
        price: item.price,
        capacity: item.capacity,
        shortDescription: shortDescription
      }
    })
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

function redirect(roomID) {
  router.push({ path: `/rooms/${roomID}`})
}

console.log(itemsPaginated)

const deleteRoom = (room_id) => {
  for (let i = 0; i < mainStore.roomTypes.length; i++) {
    if(room_id == mainStore.roomTypes[i].id){
      mainStore.roomTypes.splice(i, 1)
      break
    }
  }
  console.log(mainStore.roomTypes)
}



</script>

<template>
  <CardBoxModalRoomDelete @confirm="deleteRoom" v-model="isModalDangerActive" title="Потвърдете" button="danger" button-label="Изтрий" has-cancel />

  <table>
    <thead>
      <tr>
        <th>Заглавие</th>
        <th>Описание</th>
        <th>Цена</th>
        <th>Легла</th>
        <th/>
      </tr>
    </thead>
    <tbody>
      <tr v-for="room in itemsPaginated" :key="room.id">
        <!-- <td data-label="Title">
          {{ room.title }}
        </td>
        <td data-label="Email">
          {{ room.company }}
        </td>
        <td data-label="Email">
            {{ room.company }}
        </td>         -->
        <td data-label="Title">
          {{ room.title }}
        </td>
        <td data-label="Description">
          {{ room.shortDescription }}
        </td>
        <td data-label="Price">
          {{ room.price }}
        </td>
        <td data-label="Capacity">
          {{ room.capacity }}
        </td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton color="info" :icon="mdiPencil" small @click="redirect(room.id)" />
            <BaseButton
              color="danger"
              :icon="mdiTrashCan"
              small
              @click="() => {
                isModalDangerActive.active = true
                isModalDangerActive.id = room.id
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
