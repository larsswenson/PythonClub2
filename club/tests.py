from django.test import TestCase
from .models import Meeting, MeetingType, Resource, Event
from .forms import ResourceForm, MeetingForm

# Create your tests here.

class MeetingTypeTest(TestCase):
   def test_string(self):
       type=MeetingType(typename="meetingtype")
       self.assertEqual(str(type), type.typename)

   def test_table(self):
       self.assertEqual(str(MeetingType._meta.db_table), "meetingtype")

class MeetingTest(TestCase):
   #set up one time sample data
   def setup(self):
       type = MeetingType(typename='meetingtype')
       meeting=Meeting(meetingtitle='Meeting1', meetingagenda='Agenda1', meetinglocation='Location1')
       return meeting

   def test_string(self):
       meet = self.setup()
       self.assertEqual(str(meet), meet.meetingtitle)

   def test_type(self):
       meet=self.setup()
       self.assertEqual(str(meet.meetingtitle), 'Meeting1')

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
   def test_string(self):
       res=Resource(resourcename="Resource1")
       self.assertEqual(str(res), res.resourcename)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resourcename')

class EventTest(TestCase):
   def test_string(self):
       event=Event(eventtitle="Event1")
       self.assertEqual(str(event), event.eventtitle)

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'eventtitle')

class NewResourceForm(TestCase):
   def test_resourceform(self):
       form=ResourceForm(data={'resourcename': 'resource3', 
                               'resourcetype' : 'type3', 
                               'resourceurl': 'http://resource3.org', 
                               'resourcedateentered': '2022-05-16', 
                               'resourceuserid': 'user1', 
                               'resourcedescription': 'description3'})
       self.assertTrue(form.is_valid())

class NewMeetingForm(TestCase):
   def test_meetingform(self):
       form=MeetingForm(data={'meetingtitle': 'meeting3', 
                              'meetingdate' : '2022-05-17', 
                              'meetingtime': '03:29:23', 
                              'meetinglocation': 'location3', 
                              'meetingagenda': 'agenda3'})
       self.assertTrue(form.is_valid())

def test_meetingform_minus_location(self):
        form=MeetingForm(data={'meetinglocation': "location3"})
        self.assertTrue(form.is_valid())

def test_meetingform_empty(self):
        form=MeetingForm(data={'meetingtitle': ""})
        self.assertFalse(form.is_valid())