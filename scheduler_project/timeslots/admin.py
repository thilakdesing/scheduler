from django.contrib import admin

from timeslots.models import Timeslots

class TimeslotsAdmin(admin.ModelAdmin):
    fields = ['from_time','to_time' ]

admin.site.register(Timeslots, TimeslotsAdmin)