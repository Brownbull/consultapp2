from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AppointmentViewSet
from .views import DoctorViewSet
from .views import PatientViewSet

router = DefaultRouter()
router.register(r"doctors", DoctorViewSet)
router.register(r"patients", PatientViewSet)
router.register(r"appointments", AppointmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
