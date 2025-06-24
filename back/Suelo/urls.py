from django.urls import path
from .views import SoilAnalysisListCreateAPIView, SoilAnalysisRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('soil-analyses/', SoilAnalysisListCreateAPIView.as_view(), name='soil-analysis-list-create'),
    path('soil-analyses/<int:pk>/', SoilAnalysisRetrieveUpdateDestroyAPIView.as_view(), name='soil-analysis-detail'),
]
