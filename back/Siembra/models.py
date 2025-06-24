from django.db import models
from Productos.models import Product
from Suelo.models import SoilAnalysis
# Información de una siembra.
class Sowing(models.Model):
    name = models.CharField(max_length=100)           # Nombre de la siembra
    quantity = models.FloatField()                    # Cantidad sembrada
    area = models.FloatField(help_text="In m2")       # Área sembrada
    estimated_investment = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # Inversión estimada
    product = models.ForeignKey(Product, on_delete=models.CASCADE)         # Producto sembrado
    method = models.CharField(                                              # Método de siembra
        max_length=20,
        choices=[('MANUAL', 'Manual'), ('MECANIZED', 'Mechanized')]
    )
    date = models.DateField()                                              # Fecha de siembra
    soil_analysis = models.ForeignKey(SoilAnalysis, on_delete=models.CASCADE)  # Análisis de suelo
    greenhouse = models.BooleanField(default=False)                        # Si es en invernadero
    season = models.CharField(max_length=20, default="2025-A")            # Temporada
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Ubicación
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)                  # Fecha de creación