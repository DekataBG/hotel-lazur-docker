<script setup>
import { mdiBed } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import FormFilePicker from '@/components/FormFilePicker.vue'
import { useMainStore } from '@/stores/main'
import { ref, reactive } from 'vue'
import axios from 'axios'

const props = defineProps({
    roomId: {
        type: String,
        default: '-1'
    }
})

const mainStore = useMainStore()

const roomType = ref({})

if (props.roomId == -1){
  roomType.value.id = -1
  roomType.value.title = ''
  roomType.value.description = ''
  roomType.value.features = ''
  roomType.value.price = 0
  roomType.value.capacity = 0
  roomType.value.imagePath = ''
}
else{
  const dbRoomType = mainStore.roomTypes.filter((type) => {
    return type.id == props.roomId
  })[0]
  if (dbRoomType){
    roomType.value.id = dbRoomType.id
    roomType.value.title = dbRoomType.title
    roomType.value.description = dbRoomType.description
    roomType.value.features = dbRoomType.features
    roomType.value.price = dbRoomType.price
    roomType.value.capacity = dbRoomType.capacity
    roomType.value.imagePath = dbRoomType.imagePath
  }
  else{
    location.href = '/#/rooms'
  }
}

const submit = async () => {
  // validation?
  // confirmation modal?
  if (roomType.value.id == -1){
    await axios.post(`http://127.0.0.1:8000/room_types`, roomType.value)
  }
  else{
    await axios.put(`http://127.0.0.1:8000/room_types/${roomType.value.id}`, roomType.value)
  }
  location.reload()
}

const reset = () => {
  location.reload()
}

const imagePickerForm = reactive({
  file: null
})
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiBed" title="Редактирайте стая" main>
      </SectionTitleLineWithButton>
      <CardBox room-type @submit="submit" @reset="reset">
        <FormField label="Заглавие">
          <FormControl v-model="roomType.title" />
        </FormField>

        <FormField label="Описание">
          <FormControl v-model="roomType.description" type="textarea" />
        </FormField>

        <FormField label="Цена" help="Не въвеждайте валута">
            <FormControl v-model="roomType.price" />
        </FormField>

        <FormField label="Снимка" help="Изберете снимка">
          <FormFilePicker @updateFile="(fileName) => { roomType.imagePath = fileName}" v-model="imagePickerForm" label="Качи" :image-name="roomType.imagePath" />
        </FormField>

        <FormField label="Брой легла">
            <FormControl v-model="roomType  .capacity"/>
        </FormField>

        <template #footer>
          <BaseButtons>
            <BaseButton type="submit" color="info" label="Запази" @click="submit"/>
            <BaseButton type="reset" color="info" outline label="Поднови" @click="reset"/>
          </BaseButtons>
        </template>
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>
