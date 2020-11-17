from django.db import models
from rest_framework.renderers import JSONRenderer

class Race(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class DataPoint(models.Model):
    race = models.ForeignKey(Race, related_name="data_points", on_delete=models.CASCADE)
    time = models.TimeField()
    class Meta:
        ordering = ['time']

#datapoint elements
class GPSData(models.Model):
    data_point = models.OneToOneField(DataPoint, related_name="gps_data", on_delete=models.CASCADE)
    time = models.IntegerField(null=True)
    date = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    latitude_direction = models.CharField(max_length=3)
    longitude = models.FloatField(null=True)
    longitude_direction = models.CharField(max_length=3)
    speed_over_ground = models.FloatField(null=True)
    track_angle = models.FloatField(null=True)
    horizontal_dilutions = models.FloatField(null=True)
    altitude_over_msl = models.FloatField(null=True)
    error_of_msl = models.FloatField(null=True)

class AccelerometerData(models.Model):
    data_point = models.OneToOneField(DataPoint, related_name="accel_data", on_delete=models.CASCADE)
    time = models.IntegerField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)

class GyroscopeData(models.Model):
    data_point = models.OneToOneField(DataPoint, related_name="gyro_data", on_delete=models.CASCADE)
    time = models.IntegerField(null=True)
    pitch = models.FloatField(null=True)
    yaw = models.FloatField(null=True)
    roll = models.FloatField(null=True)

class TemperatureData(models.Model):
    data_point = models.OneToOneField(DataPoint, related_name="temp_data", on_delete=models.CASCADE)
    time = models.IntegerField(null=True)
    water_temperature = models.FloatField(null=True)
    air_temperature = models.FloatField(null=True)
    device_temperature = models.FloatField(null=True)
    battery_temperature = models.FloatField(null=True)

class WindData(models.Model):
    data_point = models.OneToOneField(DataPoint, related_name="wind_data", on_delete=models.CASCADE)
    time = models.IntegerField(null=True)
    speed = models.FloatField(null=True)
    angle = models.FloatField(null=True) # wind direction, ref from the boat's forward

class WaterData(models.Model):
    data_point = models.OneToOneField(DataPoint, related_name="water_data", on_delete=models.CASCADE)
    time = models.IntegerField(null=True)
    speed = models.FloatField(null=True)
