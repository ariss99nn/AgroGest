<template>
    <div>
        <h1>Lista de Usuarios (Solo ADMIN)</h1>
        <p v-if="loading">Cargando usuarios...</p>
        <p v-if="error">{{ error }}</p>
        <ul v-if="users.length">
            <li v-for="user in users" :key="user.id">
                {{ user.username }} ({{ user.role }}) - {{ user.email }}
            </li>
        </ul>
        <p v-else-if="!loading && !error">No hay usuarios para mostrar o no tienes permiso.</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../../../Api/axios.js'; // Tu instancia de Axios configurada

const users = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
    try {
        const response = await api.get('/users/'); // Petición a tu endpoint UserListCreateAPIView
        users.value = response.data;
    } catch (err) {
        console.error('Error al obtener usuarios:', err);
        error.value = 'No se pudieron cargar los usuarios. Puede que no tengas permisos.';
    } finally {
        loading.value = false;
    }
});
</script>