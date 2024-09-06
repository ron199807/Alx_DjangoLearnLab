from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    crop_health_index = models.FloatField()

    def __str__(self):
        return f"Data at {self.timestamp}"

class CropPrediction(models.Model):
    data = models.OneToOneField(SensorData, on_delete=models.CASCADE)
    yield_prediction = models.FloatField()
    recommendation = models.TextField()

    def __str__(self):
        return f"Prediction for {self.data.timestamp}"

