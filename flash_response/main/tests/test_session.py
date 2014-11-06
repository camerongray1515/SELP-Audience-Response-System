import uuid

from django.test import TestCase, Client

class TestSesson(TestCase):
    fixtures = ['basic_setup.json']
    
    def setUp(self):
        # Create our client, login and select a course
        self.client = Client()
        self.client.post('/login/', {'username': 'tutor1', 'password': '1234'})
        self.client.post('/tutor/select_course/', {'course': 1}, follow=True)

    # If no name is specified, an error should be displayed
    def test_session_create_missing_name(self):
        response = self.client.post('/tutor/sessions/new/', {'session-title': ''})
        self.assertContains(response, 'You must specify a title for this session')