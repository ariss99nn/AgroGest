from rest_framework import serializers
from .models import EconomicCalculation, EconomicIndicator

class EconomicCalculation_Serializer(serializers.Serializer):
    class Meta:
        model = EconomicCalculation
        fields = '__all__'

class EconomicIndicator_Serializer(serializers.Serializer):
    class Meta:
        model = EconomicIndicator
        fields = '__all__'