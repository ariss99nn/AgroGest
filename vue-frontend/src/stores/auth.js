// Importamos defineStore para crear una store de Pinia
import { defineStore } from 'pinia'
// Importamos la instancia personalizada de Axios
import api from '../api/api.js' // Asegúrate de que la ruta es correcta

export const useAuthStore = defineStore('auth', {
    state: () => ({
        accessToken: localStorage.getItem('access_token') || null,
        refreshToken: localStorage.getItem('refresh_token') || null,
        isAuthenticated: !!localStorage.getItem('access_token'),
        user: null,
    }),

    actions: {
        //recibe credenciales y obtiene tokens
        async login(credentials) {
            try {
            const response = await api.post('/token/', credentials)

        this.accessToken = response.data.access
        this.refreshToken = response.data.refresh
        this.isAuthenticated = true

        localStorage.setItem('access_token', this.accessToken)
        localStorage.setItem('refresh_token', this.refreshToken)

        await this.fetchUser()

        return true
        } catch (error) {
        console.error('Login failed:', error.response?.data || error.message)
        this.logout()
        throw error
        }
    },

    //renueva el access token
    async refreshToken() {
        if (!this.refreshToken) {
        throw new Error('No refresh token available.')
        }

        try {
        const response = await api.post('/token/refresh/', {
            refresh: this.refreshToken,
        })

        this.accessToken = response.data.access

        if (response.data.refresh) {
            this.refreshToken = response.data.refresh
            localStorage.setItem('refresh_token', this.refreshToken)
        }

        localStorage.setItem('access_token', this.accessToken)
        this.isAuthenticated = true
        return true
        } catch (error) {
        console.error('Refresh token failed:', error.response?.data || error.message)
        this.logout()
        throw error
        }
    },

    // 🚪 LOGOUT: limpia la sesión
    logout() {
        this.accessToken = null
        this.refreshToken = null
        this.isAuthenticated = false
        this.user = null
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
    },

    // 👤 FETCH USER: obtiene los datos del usuario autenticado
    async fetchUser() {
        if (this.isAuthenticated && !this.user) {
        try {
            const response = await api.get('/users/me/')
            this.user = response.data
        } catch (error) {
            console.error('Failed to fetch user data:', error)
          // this.logout() // Puedes descomentar si quieres cerrar sesión si falla
        }
        }
    }
    },

    getters: {
        isAdmin: (state) => state.user?.role === 'ADMIN',
    // Puedes añadir más getters para roles u otras condiciones
    }
})
