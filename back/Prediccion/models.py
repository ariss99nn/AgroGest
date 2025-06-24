from django.db import models
from Siembra.models import Sowing
from Usuario.models import User

# Create your models here.
# Resultado de una predicción generada por un modelo de IA.
class Prediction(models.Model):
    model = models.CharField(max_length=100)                     # Nombre del modelo de IA
    result = models.JSONField()                                  # Resultado de la predicción
    date = models.DateTimeField(auto_now_add=True)               # Fecha de creación
    sowing = models.ForeignKey(Sowing, on_delete=models.CASCADE, null=True, blank=True)  # Siembra relacionada
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)           # Usuario que generó la predicción