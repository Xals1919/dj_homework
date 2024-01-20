# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# class SensorsView(APIView):
#     def get(self, request):
#         sensor = Sensor.objects.all()
#         ser = SensorSerializer(sensor, many=True)
#         return Response(ser.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         ser = SensorSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)

# class MeasurementView(APIView):
#     def post(self, request):
#         serializer = MeasurementSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SensorDetailsView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
