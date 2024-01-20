from measurement.views import SensorsView, MeasurementView, SensorDetailsView
from django.urls import path

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorDetailsView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
