from django.urls import path
from .views import *

urlpatterns = [
    path('doc-appointment-view/',DoctorAppointmentView.as_view(),name='doc-appointment-view'),
    # hi
]
