from django.conf import settings
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.specialty})"


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} \
            (born {self.birthdate.strftime('%Y-%m-%d')})"


class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} - \
            {self.doctor} with {self.patient}"
