from django.urls import path
from .views import (
    Harvest_List_View,
    Harvest_Details_view,
    
    Classification_List_view,
    Classification_Details_View,
    
    Harvest_Type_List,
    Harvest_Type_Details_List,
    
    Harvest_Details_List,
    Harvest_Details_Detail_List,
)

urlpatterns = [
    # Harvest
    path('harvests/', Harvest_List_View.as_view(), name='harvest-list'),
    path('harvests/<int:pk>/', Harvest_Details_view.as_view(), name='harvest-detail'),

    # Classification
    path('classifications/', Classification_List_view.as_view(), name='classification-list'),
    path('classifications/<int:pk>/', Classification_Details_View.as_view(), name='classification-detail'),

    # Harvest Types
    path('harvest-types/', Harvest_Type_List.as_view(), name='harvest-type-list'),
    path('harvest-types/<int:pk>/', Harvest_Type_Details_List.as_view(), name='harvest-type-detail'),

    # Harvest Details
    path('harvest-details/', Harvest_Details_List.as_view(), name='harvest-details-list'),
    path('harvest-details/<int:pk>/', Harvest_Details_Detail_List.as_view(), name='harvest-details-detail'),
]
