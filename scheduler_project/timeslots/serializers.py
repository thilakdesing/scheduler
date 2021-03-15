from rest_framework import serializers
from timeslots.models import Timeslots

class TimeslotSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Timeslots
        fields = ('from_time','to_time')