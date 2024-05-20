import {
  mdiMonitor,
  mdiTable,
  mdiBed,
  mdiBook
} from '@mdi/js'

export default [
  {
    to: '/dashboard',
    label: 'Начало',
    icon: mdiMonitor
  },
  {
    to: '/messages',
    label: 'Съобщения',
    icon: mdiTable
  },
  {
    to: '/rooms',
    label: 'Стаи',
    icon: mdiBed
  },
  {
    to: '/reservations',
    label: 'Резервации',
    icon: mdiBook
  }
]
