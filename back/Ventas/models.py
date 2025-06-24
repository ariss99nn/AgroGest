from django.db import models

# Create your models here.
# Información financiera de una venta.
class Sale(models.Model):
    investment = models.DecimalField(max_digits=12, decimal_places=2)  # Monto invertido
    sale_price = models.DecimalField(max_digits=12, decimal_places=2)  # Precio de venta
    balance = models.DecimalField(max_digits=12, decimal_places=2)     # Balance (ganancia/pérdida)
    profitability = models.FloatField()                                # Rentabilidad
    balance_date = models.DateField()                                  # Fecha del balance
    season = models.CharField(max_length=20, default="2025-A")         # Temporada
    created_at = models.DateTimeField(auto_now_add=True)               # Fecha de creación