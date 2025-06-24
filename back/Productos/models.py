from django.db import models

# Representa un producto agrícola.
class Product(models.Model):
    name = models.CharField(max_length=100)  # Nombre del producto
    plant_spacing = models.FloatField(help_text="In meters")  # Distancia entre plantas
    market_price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de mercado
    quantity_per_area = models.FloatField(help_text="Plant/m2 ratio")  # Relación planta por m²
    unit_of_measure = models.CharField(                              # Unidad de medida utilizada
        max_length=20,
        choices=[('kg', 'Kilograms'), ('L', 'Liters'), ('m2', 'Square meters')]
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    usd_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)

