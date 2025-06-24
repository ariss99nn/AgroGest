from rest_framework import serializers
from .models import Prediction


class predictionSerializer(serializers.ModelSerializer):
    class Meta:
        model: Prediction
        fields = '__all__'

