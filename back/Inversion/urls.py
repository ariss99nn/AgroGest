from django.urls import path
from .views import Investment_List_View, Investment_Detail_View

urlpatterns = [
    path('investments/', Investment_List_View.as_view(), name='investment-list'),
    path('investments/<int:pk>/', Investment_Detail_View.as_view(), name='investment-detail'),
]