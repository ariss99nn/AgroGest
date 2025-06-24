from django.db import models

class DailyStats(models.Model):
    date = models.DateField(unique=True)
    total_sowings = models.PositiveIntegerField(default=0)
    total_soil_analyses = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.date}"
