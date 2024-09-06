
from django.contrib import admin
from django.urls import path, include
from monitoring.views import SensorDataListCreateView, CropPredictionListCreateView

urlpatterns = [
    path('sensor-data/', SensorDataListCreateView.as_view(), name='sensor-data'),
    path('predictions/', CropPredictionListCreateView.as_view(), name='predictions'),
    path('admin/', admin.site.urls),
    path('api/', include('monitoring.urls')),
]
