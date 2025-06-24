// Importamos defineStore para crear una store de Pinia
import { defineStore } from 'pinia'
// Importamos axios para hacer peticiones HTTP
import axios from 'axios'
// Importamos una instancia personalizada de axios (si tienes interceptores configurados)
// import api from '../Api/axios' // Asegúrate de que el archivo exista o usa axios directamente

// Usamos axios directamente para las peticiones de login/refresh para evitar el interceptor en bucle

// Definimos la store llamada "auth"
export const useAuthStore = defineStore('auth', {
  // -------------------------------
  // 🔷 STATE: valores reactivos globales
  // -------------------------------
    state: () => ({
    // Token de acceso desde localStorage (para mantener sesión)
        accessToken: localStorage.getItem('access_token') || null,
    // Token de refresco desde localStorage
        refreshToken: localStorage.getItem('refresh_token') || null,
    // Estado de autenticación basado en si existe un access_token
        isAuthenticated: !!localStorage.getItem('access_token'),
    // Información del usuario logueado (nombre, rol, email, etc.)
        user: null,
    }),

  // -------------------------------
  // 🔹 ACTIONS: funciones que modifican el estado o hacen lógica
  // -------------------------------
    actions: {
    // 🔐 LOGIN: recibe las credenciales y obtiene el token
    async login(credentials) {
        try {
        // Enviamos los datos al endpoint de login de Django
        const response = await axios.post('http://localhost:8000/api/token/', credentials)

        // Guardamos tokens y estado
        this.accessToken = response.data.access
        this.refreshToken = response.data.refresh
        this.isAuthenticated = true

        // Persistimos en localStorage
        localStorage.setItem('access_token', this.accessToken)
        localStorage.setItem('refresh_token', this.refreshToken)

        // Cargamos información del usuario (si el login no la trajo)
        await this.fetchUser()

        return true // Login exitoso
    } catch (error) {
        console.error('Login failed:', error.response?.data || error.message)
        this.logout() // Limpiamos todo si falla
        throw error // Propagamos el error para mostrarlo en el frontend
    }
},

    // 🔄 REFRESH TOKEN: obtiene un nuevo access token usando el refresh token
    async refreshToken() {
    if (!this.refreshToken) {
        throw new Error('No refresh token available.')
    }

    try {
        const response = await axios.post('http://localhost:8000/api/token/refresh/', {
        refresh: this.refreshToken,
        })

        // Guardamos el nuevo access token
        this.accessToken = response.data.access

        // Si el backend envía también un nuevo refresh, lo actualizamos
        if (response.data.refresh) {
        this.refreshToken = response.data.refresh
        localStorage.setItem('refresh_token', this.refreshToken)
        }

        // Guardamos el nuevo token en localStorage
        localStorage.setItem('access_token', this.accessToken)
        this.isAuthenticated = true
        return true
    } catch (error) {
        console.error('Refresh token failed:', error.response?.data || error.message)
        this.logout() // Si falla, se cierra la sesión
        throw error
    }
},

    // 🚪 LOGOUT: borra todo lo relacionado a la sesión
    logout() {
    this.accessToken = null
    this.refreshToken = null
    this.isAuthenticated = false
    this.user = null
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    },

    // 👤 FETCH USER: obtiene los datos del usuario desde la API
    async fetchUser() {
    if (this.isAuthenticated && !this.user) {
        try {
        const response = await axios.get('http://localhost:8000/api/users/me/', {
            headers: { Authorization: `Bearer ${this.accessToken}` },
        })
        this.user = response.data
        } catch (error) {
        console.error('Failed to fetch user data:', error)
          // Puedes forzar logout si prefieres cerrar sesión si falla
          // this.logout()
        }
    }
    },
},

  // -------------------------------
  // 🔸 GETTERS: funciones para acceder a propiedades calculadas
  // -------------------------------
getters: {
    // Verifica si el usuario tiene rol ADMIN
    isAdmin: (state) => state.user?.role === 'ADMIN',
    // Verifica si el usuario tiene rol EMPLOYEE
    // isEmployee: (state) => state.user?.role === 'EMPLOYEE',
    // // Verifica si el usuario tiene rol CLIENT
    // isClient: (state) => state.user?.role === 'CLIENT',
}
})