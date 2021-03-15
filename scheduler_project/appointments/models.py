from django.db import models
from timeslots.models import Timeslots
from django.contrib.auth.models import User

# Create your models here.

DAYS_MAPPING = [('SUNDAY', 'SUNDAY'),
                ('MONSDAY', 'MONSDAY'),
                ('TUESDAY', 'TUESDAY'),
                ('WEDNESDAY', 'WEDNESDAY'),
                ('THURSDAY', 'THURSDAY'),
                ('FRIDAY', 'FRIDAY'),
                ('SATURDAY', 'SATURDAY'),
                ]

class Days(models.Model):
    """
        Days of the week. Added as model to avoid hardcoding
    """
    day = models.CharField(max_length=120, default='MONDAY', choices=DAYS_MAPPING)
    def __str__(self):
        return self.day
 
    def __unicode__(self):
        return self.day
    
class Appointments(models.Model):
    """
        User as a foreign key would have roles (Doctor/Therapist)
        Staffs can either choose a selective date with timeslots or choose days of the week
        Repeat weekly is a checkbox field in Django admin which adds next week data to appointments
    """
    
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    timeslot = models.ManyToManyField(Timeslots)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    days = models.ManyToManyField(Days,null=True,blank=True)
    repeat_weekly = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True,null=True)
    created_by=models.CharField(max_length=30, default='',null=True)
    modified_datetime = models.DateTimeField(auto_now=True,null=True)
    modified_by=models.CharField(max_length=30, default='',null=True)
    
class AppointmentsManager(object):

    def handle_new_appointment(self,user,from_date,to_date):
        
        user_appointments = Appointments.objects.filter(user=user)
        if user_appointments:
            for appointment in user_appointments:
                if from_date > appointment.from_date and from_date < appointment.to_date:
                    #There's an existing appointment. Need to split the appointments or reject
                    pass