from django.db import models

# Clasificación o categoría de un producto o variedad.
class Classification(models.Model):
    variety = models.CharField(max_length=100)       # Nombre de la variedad
    classification = models.CharField(max_length=100)  # Tipo de clasificación
    details = models.TextField()                     # Detalles adicionales
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor estimado
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación


# Tipo de cosecha relacionada con una clasificación específica.
class Harvest_Type(models.Model):
    name = models.CharField(max_length=100)           # Nombre del tipo de cosecha
    start_date = models.DateField()                   # Fecha de inicio
    end_date = models.DateField()                     # Fecha de fin
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)  # Clasificación asociada
    season = models.CharField(max_length=20, default="2025-A")  # Temporada
    created_at = models.DateTimeField(auto_now_add=True)        # Fecha de creación
    
# Información de una cosecha específica.
class Harvest(models.Model):
    name = models.CharField(max_length=100)  # Nombre de la cosecha
    quantity = models.FloatField()           # Cantidad obtenida
    harvest_method = models.CharField(       # Método de recolección
        max_length=20,
        choices=[('MANUAL', 'Manual'), ('MECANIZED', 'Mechanized')]
    )
    type = models.ForeignKey(Harvest_Type, on_delete=models.CASCADE)  # Tipo de cosecha
    season = models.CharField(max_length=20, default="2025-A")       # Temporada
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)   # Ubicación GPS
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)             # Fecha de creación

# Detalles de calidad y rentabilidad de una cosecha.
class Harvest_Details(models.Model):
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)  # Clasificación del producto
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)        # Precio estimado
    profit_margin = models.FloatField()                                           # Margen de ganancia
    overall_quality = models.CharField(max_length=100)                            # Calidad general
    diagram_data = models.JSONField()                                             # Datos visuales (diagrama o gráfico)
    created_at = models.DateTimeField(auto_now_add=True)                          # Fecha de creación
    
