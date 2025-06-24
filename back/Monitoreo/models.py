from django.db import models
from Siembra.models import Sowing

# Create your models here.
# Seguimiento y observaciones sobre un cultivo.
class CropMonitoring(models.Model):
    reason = models.CharField(max_length=150)        # Motivo del monitoreo
    description = models.TextField()                 # Descripción del estado o problema
    date = models.DateField()                        # Fecha del monitoreo
    solution = models.TextField()                    # Solución aplicada
    sowing = models.ForeignKey(Sowing, on_delete=models.CASCADE)  # Siembra relacionada
    created_at = models.DateTimeField(auto_now_add=True)            # Fecha de creación