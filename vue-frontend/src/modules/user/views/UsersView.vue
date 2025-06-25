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
    <div class="p-6">
    <button @click="descargarExcel"
            class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
        Descargar Excel de Usuarios
    </button>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../../../api/api.js'; // Tu instancia de Axios configurada

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

const descargarExcel = async () => {
    try {
    const response = await api.get('/users/export_excel/', {
      responseType: 'blob'  // 👈 Necesario para archivos binarios
    })

    const blob = new Blob([response.data], {
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    })

    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', 'usuarios.xlsx') // Nombre que verá el usuario
    document.body.appendChild(link)
    link.click()
    link.remove()
    window.URL.revokeObjectURL(url)
    } catch (error) {
    console.error('Error al exportar Excel:', error)
    alert('Error al descargar el archivo.')
    }
}
</script>