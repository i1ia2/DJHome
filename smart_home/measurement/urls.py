from django.urls import path
from .views import SensorListCreateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('sensors/', SensorListCreateView., name='sensors'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensors/<int:sensor_id>/measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]
