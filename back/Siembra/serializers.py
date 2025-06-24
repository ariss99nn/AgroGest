from rest_framework import serializers
from .models import Sowing

class SowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sowing
        fields = '__all__'
