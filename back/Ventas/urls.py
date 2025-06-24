from django.urls import path
from .views import SaleListCreateAPIView, SaleRetrieveUpdateDestroyAPIView

urlpatterns = [
    # URL para listar todas las ventas y crear una nueva
    path('sales/', SaleListCreateAPIView.as_view(), name='sale-list-create'),

    # URL para obtener, actualizar o eliminar una venta específica por id
    path('sales/<int:pk>/', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale-detail'),
]
