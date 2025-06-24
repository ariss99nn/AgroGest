from rest_framework import serializers
from .models import SoilAnalysis

class SoilAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilAnalysis
        fields = '__all__'