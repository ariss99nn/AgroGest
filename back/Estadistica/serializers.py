from rest_framework import serializers
from .models import DailyStats

class Monitoring_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStats#seleciionamos el modelo de seguimiento
        fields = '__all__'