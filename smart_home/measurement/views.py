# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Sensor, TemperatureMesurement
from .serializers import SensorSerializer, SensorListSerializer, TemperatureMeasurementSerializer
@api_view
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorListSerializer
        return SensorSerializer

    def perform_create(self, serializer):
        serializer.save()

class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementCreateView(generics.CreateAPIView):
    serializer_class = TemperatureMeasurementSerializer
    queryset = TemperatureMesurement.objects.all()

    def perform_create(self, serializer):
        sensor_id = self.kwargs['pk']
        sensor = Sensor.objects.get(pk=sensor_id)
        serializer.save(sensor=sensor)