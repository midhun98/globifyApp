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

    def get_queryset(self):
        queryset = Patients.objects.all()
        hospital_id = self.request.query_params.get('hospital', None)
        if hospital_id is not None:
            queryset = queryset.filter(hospital_id=hospital_id)
        return queryset

class HospitalViewset(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
