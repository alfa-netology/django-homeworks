from django.contrib import admin
from django.urls import path, include

from measurements.api_views import ProjectViewSet, MeasurementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("measurements", MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
