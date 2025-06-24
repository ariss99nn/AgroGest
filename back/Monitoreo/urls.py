from django.urls import path
from .views import CropMonitoring_List_View, CropMonitoring_Detail_View

urlpatterns = [
    path('crop-monitorings/', CropMonitoring_List_View.as_view(), name='crop-monitoring-list'),
    path('crop-monitorings/<int:pk>/', CropMonitoring_Detail_View.as_view(), name='crop-monitoring-detail'),
]
