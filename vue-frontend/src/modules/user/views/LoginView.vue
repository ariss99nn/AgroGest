<template>
  <div>
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="loginView">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
      <p v-if="error" style="color: red;">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../../../stores/auth.js'; // Pinia

const username = ref('');
const password = ref('');
const error = ref(null);
const router = useRouter();
const authStore = useAuthStore();

async function loginView() {
  error.value = null;
  try {
    await authStore.login({ username: username.value, password: password.value });
    router.push('/');
  } catch (err) {
    error.value = 'Credenciales inválidas o error de red. Por favor, inténtalo de nuevo.';
    console.error('Login error:', err);
  }
}
</script>
