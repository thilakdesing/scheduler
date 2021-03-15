from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from appointments.models import AppointmentsManager
from appointments.serializers import AppointmentsSerializer
import datetime

class CheckAppointmentsAvailability(APIView):
    permission_classes = (IsAuthenticated,)

    def __init__(self, **kwargs):
        self.context_dict = {}

    
    def post(self, request):
        return Response({'error': 'POST method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request):
        return Response({'error': 'PUT method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def __validate_request(self,request):
        try:
            request_data = {
                        'date':request.GET['date'],
                        'from_time':request.GET['from_time'],
                        'to_time':request.GET['to_time'],
                        }
        except Exception as ex:
            return False
        
        request_data['date'] = datetime.datetime.strptime(request_data.get('date'), '%Y-%m-%d')
        request_data['from_time'] = datetime.datetime.strptime(request_data.get('from_time'), '%H:%M').time()
        request_data['to_time'] = datetime.datetime.strptime(request_data.get('to_time'), '%H:%M').time()
        return request_data
        
    def get(self, request, *args, **kwargs):
        """
        Incoming data to API
            :date: Date string of format YYYY-mm-dd 
            :from_time: Time string of format HH:MM
            :to_time: Time string of format HH:MM
        """
        
        request_data = self.__validate_request(request)
        if not request_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        results=AppointmentsManager().get_available_appoinments(request_data)
        serializer = AppointmentsSerializer(results,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)