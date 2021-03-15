from django.contrib import admin

from appointments.models import Appointments,Days,AppointmentsManager

class DaysAdmin(admin.ModelAdmin):
    fields = ['day', ]

admin.site.register(Days, DaysAdmin)

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['user','show_timeslots','from_date','to_date','show_days','repeat_weekly' ]
    fields = ['user','timeslot','from_date','to_date','days','repeat_weekly' ]


    def show_timeslots(self,obj):
        slots=[]
        for p in obj.timeslot.all():
            slots.append(p)
        return slots
    
    def save_model(self, request, obj, form, change):
        import pdb;pdb.set_trace();
        AppointmentsManager().handle_new_appointment(obj.user,obj.from_date,obj.to_date)

        if obj._state.adding:
            obj.created_by=request.user.username
        else:
            obj.modified_by=request.user.username
    
    def show_days(self,obj):
        
        return "\n".join([p.day for p in obj.days.all()])
admin.site.register(Appointments, AppointmentsAdmin)