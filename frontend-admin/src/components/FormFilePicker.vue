<script setup>
import { mdiUpload } from '@mdi/js'
import { computed, ref, watch } from 'vue'
import BaseButton from '@/components/BaseButton.vue'
import axios from 'axios'

const props = defineProps({
  modelValue: {
    type: [File, String],
    default: null
  },
  label: {
    type: String,
    default: null
  },
  icon: {
    type: String,
    default: mdiUpload
  },
  accept: {
    type: String,
    default: null
  },
  color: {
    type: String,
    default: 'info'
  },
  imageName: {
    type: String,
    default: ""
  },
  isRoundIcon: Boolean
})

const emit = defineEmits(['updateFile'])

const root = ref(null)

const file = ref(props.modelValue)

const modelValueProp = computed(() => props.modelValue)

watch(modelValueProp, (value) => {
  file.value = value

  if (!value) {
    root.value.input.value = null
  }
})

const upload = (event) => {
  const value = event.target.files || event.dataTransfer.files

  file.value = value[0]

  emit('updateFile', file.value.name)

  let formData = new FormData()
  formData.append('file', file.value)

  const mediaStoreRoute = 'http://127.0.0.1:8000/upload/'

  axios
    .post(mediaStoreRoute, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      onUploadProgress: progressEvent
    })
}

const uploadPercent = ref(0)

const progressEvent = progressEvent => {
  uploadPercent.value = Math.round(
    (progressEvent.loaded * 100) / progressEvent.total
  )
}
</script>

<template>
  <div class="flex items-stretch justify-start relative">
    <label class="inline-flex">
      <BaseButton
        as="a"
        :class="{ 'w-12 h-12': isRoundIcon }"
        :icon-size="isRoundIcon ? 24 : undefined"
        :label="isRoundIcon ? null : label"
        :icon="icon"
        :color="color"
        :rounded-full="isRoundIcon"
      />
      <input
        ref="root"
        type="file"
        class="absolute top-0 left-0 w-full h-full opacity-0 outline-none cursor-pointer -z-1"
        :accept="accept"
        @input="upload"
      />
    </label>
    <div
      class="px-4 py-2 bg-gray-100 dark:bg-slate-800 border-gray-200 dark:border-slate-700 border rounded-r"
    >
      <span class="text-ellipsis line-clamp-1">
        {{  imageName }}
      </span>
    </div>
  </div>
</template>