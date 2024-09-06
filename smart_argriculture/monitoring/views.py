from rest_framework import generics
from .models import SensorData, CropPrediction
from .serializers import SensorDataSerializer, CropPredictionSerializer

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

class CropPredictionListCreateView(generics.ListCreateAPIView):
    queryset = CropPrediction.objects.all()
    serializer_class = CropPredictionSerializer


#prediction Analysis

import pandas as pd
from .models import SensorData, CropPrediction

def generate_prediction(sensor_data):
    # Simple logic to generate yield prediction and recommendation
    temp = sensor_data.temperature
    moisture = sensor_data.soil_moisture

    # Basic prediction logic (can be expanded with ML models)
    yield_prediction = (moisture / 100) * (30 - abs(temp - 25))
    recommendation = "Increase watering" if moisture < 50 else "Optimal conditions"

    return yield_prediction, recommendation



# adding a new SensorData entry

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

    def perform_create(self, serializer):
        sensor_data = serializer.save()
        yield_pred, rec = generate_prediction(sensor_data)
        CropPrediction.objects.create(data=sensor_data, yield_prediction=yield_pred, recommendation=rec)

