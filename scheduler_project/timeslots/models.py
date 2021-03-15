from django.db import models

# Create your models here.

class Timeslots(models.Model):
    """
        From time and To time for timeslots
    """
    
    from_time = models.TimeField(null=False)
    to_time = models.TimeField(null=False)
    created_datetime = models.DateTimeField(auto_now_add=True,null=True)
    created_by=models.CharField(max_length=30, default='',null=True)
    modified_datetime = models.DateTimeField(auto_now=True,null=True)
    modified_by=models.CharField(max_length=30, default='',null=True)
    
    def __str__(self):
        return str(self.from_time) +' to '+ str(self.to_time)
 
    def __unicode__(self):
        return str(self.from_time) +' to '+ str(self.to_time)