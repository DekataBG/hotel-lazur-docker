<script setup>
import { reactive } from 'vue'
import { mdiAccount, mdiAsterisk } from '@mdi/js'
import SectionFullScreen from '@/components/SectionFullScreen.vue'
import CardBox from '@/components/CardBox.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import LayoutGuest from '@/layouts/LayoutGuest.vue'
import { useMainStore } from '@/stores/main'

const form = reactive({
  username: '',
  password: '',
  remember: true
})

const mainStore = useMainStore()
const submit = (username, password) => {
  mainStore.logIn(username, password)
}
</script>

<template>
  <LayoutGuest>
    <SectionFullScreen v-slot="{ cardClass }" bg="purplePink">
      <CardBox :class="cardClass" is-form @submit.prevent="submit(form.username, form.password)">
        <FormField label="Потребителско име" help="Въведи потребителско име">
          <FormControl
            v-model="form.username"
            :icon="mdiAccount"
            name="login"
          />
        </FormField>

        <FormField label="Парола" help="Въведи парола">
          <FormControl
            v-model="form.password"
            :icon="mdiAsterisk"
            type="password"
            name="password"
          />
        </FormField>

        <template #footer>
          <BaseButtons>
            <BaseButton type="submit" color="info" label="Влез" />
          </BaseButtons>
        </template>
      </CardBox>
    </SectionFullScreen>
  </LayoutGuest>
</template>
