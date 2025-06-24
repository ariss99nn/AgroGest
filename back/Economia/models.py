from django.db import models
from Siembra.models import Sowing  # Ajusta según el nombre de tu app original

class EconomicCalculation(models.Model):
    sowing = models.OneToOneField(Sowing, on_delete=models.CASCADE)
    estimated_investment = models.DecimalField(max_digits=12, decimal_places=2)
    projected_income = models.DecimalField(max_digits=12, decimal_places=2)
    irr = models.FloatField(null=True, blank=True)
    npv = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

class EconomicIndicator(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    source = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)