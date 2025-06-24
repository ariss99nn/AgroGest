from django.urls import path
from .views import SowingListCreateAPIView, SowingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('sowings/', SowingListCreateAPIView.as_view(), name='sowing-list-create'),
    path('sowings/<int:pk>/', SowingRetrieveUpdateDestroyAPIView.as_view(), name='sowing-detail'),
]
