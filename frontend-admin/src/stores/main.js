import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

const apiLocation = 'http://127.0.0.1:8000'

export const useMainStore = defineStore('main', () => {
  const userAvatar = computed(
    () =>
      `https://api.dicebear.com/7.x/avataaars/svg?seed=${userEmail.value.replace(
        /[^a-z0-9]+/gi,
        '-'
      )}`
  )

  const isFieldFocusRegistered = ref(false)

  const clients = ref([])
  const rooms = ref([])
  const roomTypes = ref([])
  const reservations = ref([])
  const token = ref()

  function fetchSampleClients() {
    axios
      .get(apiLocation + '/messages')
      .then((result) => {
        clients.value = result?.data
      })
      .catch((error) => {
        alert(error.message)
      })
  }

  function fetchSampleRooms() {
    axios
      .get(apiLocation + '/rooms')
      .then(result => {
        rooms.value = result?.data
      })
      .catch((error) => {
        alert(error.message)
      })
  }

  function fetchSampleRoomTypes() {
    axios
      .get(apiLocation + '/room_types')
      .then(result => {
        roomTypes.value = result?.data
      })
      .catch((error) => {
        alert(error.message)
      })
  }

  function fetchSampleReservations() {
    axios
      .get(apiLocation + '/reservations')
      .then(result => {
        reservations.value = result?.data
      })
      .catch((error) => {
        alert(error.message)
      })
  }

  const router = useRouter()
  router.beforeEach((to, from) => {
    if(to.path == '/') {
      token.value = undefined
      return true
    }
    if(token.value === undefined) {
      return '/'
    }

    return true
  })

  const headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  function logIn(username, password) {
    axios
      .post(apiLocation + '/token', {
        'username': username,
        'password': password
      }, {
        headers: headers
      })
      .then((result) => {
        router.push('/dashboard')
        token.value = result?.data.access_token
      })
      .catch(() => {
        const $toast = useToast();
        $toast.open({
            message: 'Грешно потребителско име или парола',
            type: 'error',
            position: 'top'
        });

      })
  }

  return {
    userAvatar,
    isFieldFocusRegistered,
    clients,
    rooms,
    roomTypes,
    reservations,
    fetchSampleClients,
    fetchSampleRooms,
    fetchSampleRoomTypes,
    fetchSampleReservations,
    logIn
  }
})
