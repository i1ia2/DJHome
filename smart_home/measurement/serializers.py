from rest_framework import serializers
from .models import Sensor, TemperatureMesurement



# TODO: опишите необходимые сериализаторы

class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMesurement
        fields = ['temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurements = TemperatureMeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']