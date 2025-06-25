import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth.js'; // Pinia
import HomeView from '../views/HomeView.vue';
import LoginView from '../modules/user/views/LoginView.vue';
import AboutView from '../views/AboutView.vue';
import UsersView from '../modules/user/views/UsersView.vue';
import ProfileView from '../modules/user/views/ProfileView.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/about',
        name: 'About',
        component: AboutView,
    },
    {
        path: '/users',
        name: 'Users',
        component: UsersView,
    //     // meta: { requiresAuth: true, requiresAdmin: true }, // Rutas protegidas que requieren ser ADMIN
    },

    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        // meta: { requiresAuth: true }, // Ruta protegida
    },
    // ... otras rutas
];

const router = createRouter({
    // history: createWebHistory(import.meta.env.BASE_URL),
    history: createWebHistory(),
    routes,
});

 // Navigation Guard global
router.beforeEach(async (to, from, next) => {
     const authStore = useAuthStore(); // Pinia
     // const isAuthenticated = store.getters.isAuthenticated; // Vuex
     // const isAdmin = store.getters.isAdmin; // Vuex

     // Asegurarse de que el estado de autenticación se ha cargado si hay tokens en localStorage
    if (!authStore.isAuthenticated && localStorage.getItem('access_token')) {
         authStore.isAuthenticated = true; // Forzar a true para que intente refrescar
         await authStore.refreshToken().catch(() => {}); // Intenta refrescar silenciosamente si hay refresh token
    }  
     // Si la ruta requiere autenticación
    if (to.meta.requiresAuth) {
        if (!authStore.isAuthenticated) {
             // Si no está autenticado, redirige al login
            next('/login');
        } else {
             // Si está autenticado, verifica si la ruta requiere rol de ADMIN
            if (to.meta.requiresAdmin) {
                  // Si no se ha cargado el usuario, intente cargarlo (para verificar el rol)
                if (!authStore.user) {
                    await authStore.fetchUser();
                }
                if (!authStore.isAdmin) {
                     // Si no es ADMIN, redirige a una página de no autorizado o a la home
                    alert('No tienes permisos para acceder a esta sección.');
                    next('/');
                } else {
                     next(); // Permitir el acceso
                }
            } else {
                 next(); // Permitir el acceso
            }
        }
    } else {
         // Si la ruta no requiere autenticación (ej. login, home pública)
         // Y el usuario ya está autenticado, quizás redirigir de login a home
        if (to.name === 'Login' && authStore.isAuthenticated) {
            next('/');
        } else {
             next(); // Permitir el acceso
        }
    }
});

export default router;