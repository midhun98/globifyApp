# Create your models here.
from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitals"


class Patients(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    inpatient_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    outpatient_number = models.CharField(max_length=10, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.inpatient_number}"

    class Meta:
        verbose_name = "Patients"
        verbose_name_plural = "Patients"
