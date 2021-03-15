from rest_framework import serializers
from appointments.models import Appointments
from timeslots.serializers import TimeslotSerializer

class AppointmentsSerializer(serializers.ModelSerializer):
    
    timeslot = TimeslotSerializer(many=True)
    class Meta:
        
        model = Appointments
        fields = ('timeslot','timezone')