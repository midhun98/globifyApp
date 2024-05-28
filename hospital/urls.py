from django.urls import path, include
from . import views
from django.views.generic import TemplateView


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('patients', views.PatientViewSet)
router.register('hospitals', views.HospitalViewset)
urlpatterns = [
    path("", TemplateView.as_view(template_name="hospital.html"), name='hospital'),
    path("patients/<int:hospitalId>/", TemplateView.as_view(template_name="patients.html"), name='patients'),  # Add this line
    path('api/', include(router.urls)),

]