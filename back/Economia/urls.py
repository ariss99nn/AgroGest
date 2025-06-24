from django.urls import path
from .views import economic_indicators

urlpatterns = [
    path('indicators/', economic_indicators),
]