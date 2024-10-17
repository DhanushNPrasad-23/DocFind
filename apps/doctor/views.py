from django.shortcuts import render
from apps.autenticateapp.models import AppointmentModel
from apps.autenticateapp.serializers import AppointmentSerials
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DoctorAppointmentView(APIView):
    
    def get(self,request,*args, **kwargs):
        username = request.user.username
        
        obj = AppointmentModel.objects.filter(doc_name = username)
        serial = AppointmentSerials(obj,many=True)
        return Response({
            'data' : serial.data
        },status=status.HTTP_200_OK)