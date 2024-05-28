from .models import (
    Hospital,
    Patients
)
from rest_framework import viewsets
from hospital.serializers import HospitalSerializer, PatientsSerializer

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer


class HospitalViewset(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
