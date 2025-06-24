from django.db import models
# Información de insumos agrícolas utilizados.
class Input(models.Model):
    name = models.CharField(max_length=100)                    # Nombre del insumo
    description = models.TextField()                           # Descripción
    used_for = models.CharField(max_length=100)                # Uso o propósito
    application_method = models.CharField(max_length=100)      # Método de aplicación
    quantity = models.FloatField()                             # Cantidad disponible o aplicada
    unit_of_measure = models.CharField(                        # Unidad de medida
        max_length=20,
        choices=[('kg', 'Kilograms'), ('L', 'Liters')]
    )
    created_at = models.DateTimeField(auto_now_add=True)       # Fecha de creación
    usd_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # NEW
    local_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # NEW
