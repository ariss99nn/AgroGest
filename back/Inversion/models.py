from django.db import models
from Productos.models import Product

# Create your models here.
# Datos de inversión relacionada con un producto.
class Investment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Producto relacionado
    value = models.DecimalField(max_digits=12, decimal_places=2)    # Valor invertido
    irr = models.FloatField(null=True, blank=True)                  # Tasa interna de retorno (TIR)
    npv = models.FloatField(null=True, blank=True)                  # Valor actual neto (VAN)
    period = models.CharField(max_length=20, default="2025-A")      # Periodo/temporada
    created_at = models.DateTimeField(auto_now_add=True)            # Fecha de creación