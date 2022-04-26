from django.contrib import admin
from .models import MeetingType, Meeting, MeetingMinutes, Resource, Event

# Register your models here.
admin.site.register(MeetingType)
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)

