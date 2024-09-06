from rest_framework import serializers
from .models import SensorData, CropPrediction

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class CropPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropPrediction
        fields = '__all__'
