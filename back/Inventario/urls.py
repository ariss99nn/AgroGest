from django.urls import path
from .views import Input_List_View, Input_Detail_View

urlpatterns = [
    path('inputs/', Input_List_View.as_view(), name='input-list'),
    path('inputs/<int:pk>/', Input_Detail_View.as_view(), name='input-detail'),
]