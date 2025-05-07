# ruff: noqa: ERA001, E501
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .models import Doctor
from .models import Patient
from .permissions import IsDoctorOrStaff
from .serializers import AppointmentSerializer
from .serializers import DoctorSerializer
from .serializers import PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["first_name", "last_name", "specialty"]
    ordering_fields = ["last_name"]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["last_name", "birth_date"]


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrStaff]
    queryset = Appointment.objects.none()

    # Search and filter setup
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["doctor", "patient"]
    search_fields = ["notes"]
    ordering_fields = ["date"]

    # Dynamic queryset based on logged-in user ! DRF will pick this up
    def get_queryset(self):
        user = self.request.user
        if hasattr(user, "doctor"):
            return Appointment.objects.filter(doctor=user.doctor)
        return Appointment.objects.none()
