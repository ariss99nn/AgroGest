import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router.js'
import { createPinia } from 'pinia'
import { useAuthStore } from './stores/auth'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

app.mount('#app')

const authStore = useAuthStore();
if (authStore.accessToken && !authStore.user) {
  authStore.fetchUser(); // Carga info al recargar
}




// createApp(App).use(router).mount('#app')