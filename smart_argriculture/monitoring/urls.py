from django.urls import path
from .views import SensorDataListCreateView, CropPredictionListCreateView

urlpatterns = [
    path('sensor-data/', SensorDataListCreateView.as_view(), name='sensor-data'),
    path('predictions/', CropPredictionListCreateView.as_view(), name='predictions'),
]
