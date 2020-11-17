from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GPSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSData
        fields = [
            'time',
            'date',
            'latitude',
            'latitude_direction',
            'longitude',
            'longitude_direction',
            'speed_over_ground',
            'track_angle',
            'horizontal_dilutions',
            'altitude_over_msl',
            'error_of_msl'
        ]

class AccelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccelerometerData
        fields = [
            'time',
            'x',
            'y',
            'z'
        ]

class GyroDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GyroscopeData
        fields = [
            'time',    
            'pitch',
            'yaw',
            'roll'
        ]
    
class TempDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureData
        fields = [
            'time',
            'water_temperature',
            'air_temperature',
            'device_temperature',
            'battery_temperature'
        ]

class WindDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindData
        fields = [
            'time',
            'speed',
            'angle'
        ]

class WaterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterData
        fields = [
            'time',
            'speed'        
        ]

class DataPointSerializer(serializers.ModelSerializer):

    gps_data = GPSDataSerializer()
    accel_data = AccelDataSerializer()
    gyro_data = GyroDataSerializer()
    temp_data = TempDataSerializer()
    wind_data = WindDataSerializer()
    water_data = WaterDataSerializer()

    class Meta:
        model = DataPoint
        fields = [
            'time', 
            'gps_data', 
            'accel_data', 
            'gyro_data', 
            'temp_data',
            'wind_data',
            'water_data'
        ]

    def create(self, validated_data):
        gps_data = validated_data.pop('gps_data')
        accel_data = validated_data.pop('accel_data')
        gyro_data = validated_data.pop('gyro_data')
        temp_data = validated_data.pop('temp_data')
        wind_data = validated_data.pop('wind_data')
        water_data = validated_data.pop('water_data')

        dp = DataPoint.objects.create(**validated_data)

        gps_data.update({"data_point_id": dp.id})
        accel_data.update({"data_point_id": dp.id})
        gyro_data.update({"data_point_id": dp.id})
        temp_data.update({"data_point_id": dp.id})
        wind_data.update({"data_point_id": dp.id})
        water_data.update({"data_point_id": dp.id})

        GPSData.objects.create(**gps_data)
        AccelerometerData.objects.create(**accel_data)
        GyroscopeData.objects.create(**gyro_data)
        TemperatureData.objects.create(**temp_data)
        WindData.objects.create(**wind_data)
        WaterData.objects.create(**water_data)

        return dp


class RaceSerializer(serializers.HyperlinkedModelSerializer):

    #data_points = DataPointSerializer(many=True)

    class Meta:
        model = Race
        fields = [
            'url', 
            'date', 
            'name', 
            'location', 
            'description' #,'data_points'
            ]

class RaceDetailsSerializer(serializers.HyperlinkedModelSerializer):

    data_points = DataPointSerializer(many=True)

    class Meta:
        model = Race
        fields = [
            'url', 
            'date', 
            'name', 
            'location', 
            'description',
            'data_points'
            ]
