from django.contrib import admin

from appointments.models import Appointments,Days,AppointmentsManager
from rest_framework.authtoken.models import Token
class DaysAdmin(admin.ModelAdmin):
    fields = ['day', ]

admin.site.register(Days, DaysAdmin)

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['user','show_timeslots','from_date','to_date','show_days','repeat_weekly' ]
    fields = ['user','timeslot','from_date','to_date','days','timezone','repeat_weekly' ]


    def show_timeslots(self,obj):
        slots=[]
        for p in obj.timeslot.all():
            slots.append(p)
        return slots
    
    def save_model(self, request, obj, form, change):
        
        if obj._state.adding:
            obj.created_by=request.user.username
        else:
            obj.modified_by=request.user.username
        user = obj.user
        Token.objects.get_or_create(user=user)
        obj.save()
        
    def show_days(self,obj):
        
        return "\n".join([p.day for p in obj.days.all()])
admin.site.register(Appointments, AppointmentsAdmin)