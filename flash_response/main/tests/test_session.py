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

    # Add a session and then check it appears in the list of sessions
    def test_session_create(self):
        session_name = uuid.uuid4() # Get a random session name
        response = self.client.post('/tutor/sessions/new/', {'session-title': session_name}, follow=True)
        self.assertContains(response, session_name)