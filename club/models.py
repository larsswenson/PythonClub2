from django.db import models
from django.contrib.auth.models import User

class MeetingType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='meetingtype'
        verbose_name_plural='meetingtypes'

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingminutesid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingminutesattendance=models.ManyToManyField(User)
    meetingminutestext=models.TextField()

    def __str__(self):
        return self.meetingminutesid
    
    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField()
    resourceurl=models.URLField(null=True, blank=True)
    resourcedateentered=models.DateField()
    resourceuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resourcename'
        verbose_name_plural='resourcenames'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField()
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
        

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='eventtitle'
        verbose_name_plural='eventtitles'

    # Create your models here.
