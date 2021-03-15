from django.db import models
from timeslots.models import Timeslots
from django.contrib.auth.models import User
from django.db.models.signals import post_save,m2m_changed
import datetime

# Create your models here.

DAYS_MAPPING = [('SUNDAY', 'SUNDAY'),
                ('MONSDAY', 'MONSDAY'),
                ('TUESDAY', 'TUESDAY'),
                ('WEDNESDAY', 'WEDNESDAY'),
                ('THURSDAY', 'THURSDAY'),
                ('FRIDAY', 'FRIDAY'),
                ('SATURDAY', 'SATURDAY'),
                ]

TIMEZONE_MAPPING = [('','TIMEZONE1'),
                    ('TIMEZONE2','TIMEZONE2'),
                    ('TIMEZONE3','TIMEZONE3'),
    
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
    timezone = models.CharField(max_length=120, default='TIMEZONE1', choices=TIMEZONE_MAPPING)
    created_datetime = models.DateTimeField(auto_now_add=True,null=True)
    created_by=models.CharField(max_length=30, default='',null=True)
    modified_datetime = models.DateTimeField(auto_now=True,null=True)
    modified_by=models.CharField(max_length=30, default='',null=True)

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def current_weekday(d,weekday):
    days_ahead = weekday - d.weekday()
    return d + datetime.timedelta(days_ahead)
    
def post_save_receiver(sender, **kwargs):
    days =  kwargs['pk_set']
    instance = kwargs['instance']
    action = kwargs['action']
    if action == 'post_add':
        today = datetime.datetime.now().date()
        for day_number in days:
            currentweeks_date = current_weekday(today,day_number)
            nextweeks_date = next_weekday(today, day_number)  
            AppointmentsManager().create_appointments_based_on_days(currentweeks_date,instance)
            if instance.repeat_weekly == True:
                AppointmentsManager().create_appointments_based_on_days(nextweeks_date,instance)
        
m2m_changed.connect(post_save_receiver, sender=Appointments.days.through)

class AppointmentsManager(object):

    def get_available_appoinments(self, request_data):
        
        timeslot_objs = Timeslots.objects.filter(from_time__lte = request_data.get('from_time'),
                                    to_time__gte = request_data.get('to_time'))
        
        return Appointments.objects.filter(from_date__lte = request_data.get('date'),
                                    to_date__gte = request_data.get('date'),
                                    timeslot__in= timeslot_objs)
        
        
    def create_appointments_based_on_days(self,date,instance):
        new_obj = Appointments.objects.get(id=instance.id)
        new_obj.id=None
        new_obj.from_date = date
        new_obj.to_date = date
        new_obj.repeat_weekly = False
        new_obj.save()
        
        