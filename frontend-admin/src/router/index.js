import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/views/HomeView.vue'

const routes = [
  {
    meta: {
      title: 'Начало'
    },
    path: '/dashboard',
    name: 'dashboard',
    component: Home
  },
  {
    meta: {
      title: 'Съобщения'
    },
    path: '/messages',
    name: 'messages',
    component: () => import('@/views/MessagesView.vue')
  },
  {
    meta: {
      title: 'Стаи'
    },
    path: '/rooms',
    name: 'rooms',
    component: () => import('@/views/RoomsView.vue')
  },
  {
    meta: {
      title: 'Стая'
    },
    path: '/rooms/:roomId',
    props: true,
    name: 'room',
    component: () => import('@/views/RoomView.vue')
  },
  {
    meta: {
      title: 'Резервации'
    },
    path: '/reservations',
    name: 'reservations',
    component: () => import('@/views/ReservationsView.vue')
  },
  {
    meta: {
      title: 'Резервация'
    },
    path: '/reservations/:reservationId',
    props: true,
    name: 'reservation',
    component: () => import('@/views/ReservationView.vue')
  },
  {
    meta: {
      title: 'Влез'
    },
    path: '/',
    name: 'login',
    component: () => import('@/views/LoginView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
