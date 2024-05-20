<script setup>
import { computed, ref } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiEye, mdiTrashCan } from '@mdi/js'
import CardBoxModalMessageDelete from './CardBoxModalMessageDelete.vue'
import CardBoxModalMessageInfo from './CardBoxModalMessageInfo.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import UserAvatar from '@/components/UserAvatar.vue'

defineProps({
  checkable: Boolean
})

const mainStore = useMainStore()
mainStore.fetchSampleClients()

const SHORT_MESSAGE_LENGTH = 10

const items = computed(() => mainStore.clients)

const isModalActive = ref({
  active: false,
  name: 'placeholder',
  email: 'placeholder',
  message: 'placeholder'
})

const isModalDangerActive = ref({
  active: false,
  id: -1,
  email: 'placeholder'
})

const perPage = ref(10)

const currentPage = ref(0)

const itemsPaginated = computed(() =>
  items.value.map((item) => {
    let shortMessage;
    if (item.message.length > SHORT_MESSAGE_LENGTH){
      shortMessage = item.message.slice(0, 10) + '...'
    }
    else{
      shortMessage = item.message
    }
    return {id: item.id, name: item.name, email: item.email, shortMessage: shortMessage, message: item.message, sentDate: item.sentDate}
  }).slice(perPage.value * currentPage.value, perPage.value * (currentPage.value + 1))
)

console.log(itemsPaginated.value[0].message)

const numPages = computed(() => Math.ceil(items.value.length / perPage.value))

const currentPageHuman = computed(() => currentPage.value + 1)

const pagesList = computed(() => {
  const pagesList = []

  for (let i = 0; i < numPages.value; i++) {
    pagesList.push(i)
  }

  return pagesList
})

const deleteMessage = (message_id) => {
  for (let i = 0; i < mainStore.clients.length; i++) {
    if(message_id == mainStore.clients[i].id){
      mainStore.clients.splice(i, 1)
      break
    }
  }
  console.log(mainStore.clients)
}

</script>

<template>
  <CardBoxModalMessageInfo v-model="isModalActive" title="Цяло съобщение">
  </CardBoxModalMessageInfo>

  <CardBoxModalMessageDelete @confirm="deleteMessage" v-model="isModalDangerActive" title="Потвърдете" button="danger" button-label="Изтрий" has-cancel>
  </CardBoxModalMessageDelete>

  <table>
    <thead>
      <tr>
        <th />
        <th>Име</th>
        <th>Емейл</th>
        <th>Съобщение</th>
        <th>Изпратено</th>
        <th />
      </tr>
    </thead>
    <tbody>
      <tr v-for="client in itemsPaginated" :key="client.id">
        <td class="border-b-0 lg:w-6 before:hidden">
          <UserAvatar :username="client.name" class="w-24 h-24 mx-auto lg:w-6 lg:h-6" />
        </td>
        <td data-label="Name">
          {{ client.name }}
        </td>
        <td data-label="Email">
          {{ client.email }}
        </td>
        <td data-label="Message">
          {{ client.shortMessage }}
        </td>
        <td data-label="Sent" class="lg:w-1 whitespace-nowrap">
          <small class="text-gray-500 dark:text-slate-400" :title="client.sent">{{
            client.sentDate
          }}</small>
        </td>
        <td class="before:hidden lg:w-1 whitespace-nowrap">
          <BaseButtons type="justify-start lg:justify-end" no-wrap>
            <BaseButton
            color="info"
            :icon="mdiEye"
            small
            @click="() => {
              isModalActive.active = true
              isModalActive.name = client.name
              isModalActive.email = client.email
              isModalActive.message = client.message
            }" />
            <BaseButton
              color="danger"
              :icon="mdiTrashCan"
              small
              @click="() => {
                isModalDangerActive.active = true
                isModalDangerActive.id = client.id
                isModalDangerActive.email = client.email
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
