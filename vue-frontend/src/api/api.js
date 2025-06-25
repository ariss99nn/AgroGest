import axios from 'axios';
import router from '../router/router.js'; // Asumiendo que tienes un router en src/router/index.js
import { useAuthStore } from '../stores/auth.js';

const api = axios.create({
    baseURL: 'http://localhost:8000/api', // API url
    headers: {
        'Content-Type': 'application/json', //Tipo de datos que se enviará
        'Authorization': 'Token ' + localStorage.getItem('token') // Token de autenticación para acceder
    }
})
// Interceptor para añadir el token de acceso a cada petición
api.interceptors.request.use(
    (config) => {
        const authStore = useAuthStore(); // O store.state.auth.accessToken si usas Vuex
        const accessToken = authStore.accessToken;

        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Interceptor para manejar la expiración del token y el refresh
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        const authStore = useAuthStore(); // O store si usas Vuex

        // Si el error es 401 (Unauthorized) y no es la petición de refresh token original
        // Y no hemos intentado refrescar esta petición antes
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true; // Marca la petición para evitar bucles infinitos

            try {
                // Intenta refrescar el token
                await authStore.refreshToken();
                // Si el refresh es exitoso, reintenta la petición original con el nuevo token
                originalRequest.headers.Authorization = `Bearer ${authStore.accessToken}`;
                return api(originalRequest);
            } catch (refreshError) {
                // Si el refresh falla (refresh token inválido o expirado)
                console.error('Failed to refresh token. Logging out...', refreshError);
                authStore.logout(); // Limpia el estado de autenticación
                router.push('/login'); // Redirige al login
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

// Luego, en tus componentes o servicios, usarías:
// import api from './api';
// api.get('/users/me/').then(response => console.log(response.data));
export default api;