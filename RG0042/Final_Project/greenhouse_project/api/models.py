from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    TEMPERATURE = 'Temperature'
    HUMIDITY = 'Humidity'
    SOIL_MOISTURE = 'Soil Moisture'
    LIGHT = 'Light Level'

    METRIC_CHOICES = [
        (TEMPERATURE, 'Temperature'),
        (HUMIDITY, 'Humidity'),
        (SOIL_MOISTURE, 'Soil Moisture'),
        (LIGHT, 'Light Level'),
    ]

    metric_type = models.CharField(max_length=20, choices=METRIC_CHOICES)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type} - {self.value} at {self.timestamp}"


class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    temperature_threshold = models.FloatField(default=30.0)
    humidity_threshold = models.FloatField(default=70.0)
    soil_moisture_threshold = models.FloatField(default=50.0)
    light_level_threshold = models.FloatField(default=1000.0)

    def __str__(self):
        return f"Settings for {self.user.username}"
