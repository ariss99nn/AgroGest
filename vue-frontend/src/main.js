import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
// import HomeView from './views/HomeView.vue'
import router from './router/router.js'
import { createPinia } from 'pinia'


const app = createApp(App)

const pinia = createPinia()
app.use(createPinia) // 👈 importante: esto debe ir antes de usar cualquier store
app.use(router)

const authStore = useAuthStore();
if (authStore.accessToken && !authStore.user) {
  authStore.fetchUser(); // Carga info al recargar
}

app.mount('#app')


// createApp(App).use(router).mount('#app')