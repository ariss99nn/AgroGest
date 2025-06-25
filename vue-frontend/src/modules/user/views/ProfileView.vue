<template>
    <div class="max-w-md mx-auto mt-10 p-6 border rounded shadow bg-white">
    <h2 class="text-2xl font-semibold mb-4">Perfil de Usuario</h2>

    <div v-if="user">
        <p><strong>Usuario:</strong> {{ user.username }}</p>
        <p><strong>Nombre:</strong> {{ user.first_name }} {{ user.last_name }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Rol:</strong> {{ user.role }}</p>
        <p><strong>Documento:</strong> {{ user.document }}</p>
        <p><strong>Teléfono:</strong> {{ user.phone }}</p>
        <p><strong>Ciudad:</strong> {{ user.city }}</p>
        
    </div>

    <div v-else class="text-gray-500">Cargando perfil...</div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '../../../stores/auth.js'

const authStore = useAuthStore()

// Cargar perfil si aún no está
onMounted(() => {
    if (!authStore.user && authStore.isAuthenticated) {
    authStore.fetchUser()
    }
})

const user = authStore.user
</script>
