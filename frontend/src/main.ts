import './assets/style.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ToastPlugin from 'vue-toast-notification'
import 'vue-toast-notification/dist/theme-bootstrap.css'
import VueCollapsiblePanel from '@dafcoe/vue-collapsible-panel'

const app = createApp(App)

app.use(router)
app.use(store)
app.use(ToastPlugin)
app.use(VueCollapsiblePanel)

app.mount('#app')
