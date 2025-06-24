"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obtener access y refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Para renovar access token
    path('api/', include('Cosecha.urls')),
    path('api/', include('Economia.urls')),
    path('api/', include('Estadistica.urls')),
    path('api/', include('Inventario.urls')),
    path('api/', include('Inversion.urls')),
    path('api/', include('Monitoreo.urls')),
    path('api/', include('Prediccion.urls')),
    path('api/', include('Productos.urls')),
    path('api/', include('Siembra.urls')),
    path('api/', include('Suelo.urls')),
    path('api/', include('Usuario.urls')),
    path('api/', include('Ventas.urls')),
]
