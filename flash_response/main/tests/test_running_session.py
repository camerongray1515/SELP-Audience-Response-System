from django.test import TestCase, Client
from main.models import Session

class TestRunningSesson(TestCase):
    fixtures = ['basic_setup.json']
    
    def setUp(self):
        # Create our client, login and select a course
        self.client = Client()
        self.client.post('/login/', {'username': 'tutor1', 'password': '1234'})
        self.client.post('/tutor/select_course/', {'course': 1}, follow=True)

    # Get a session, start it and then check that it changes to active and that
    # the URL code changes
    def test_start_new_session(self):
        s_old = Session.objects.get(pk=1)
        s_old.running = False;
        s_old.save()

        response = self.client.get('/tutor/sessions/run/1/')

        s_new = Session.objects.get(pk=1)
        self.assertEqual(s_new.running, True)
        self.assertNotEqual(s_new.url_code, s_old.url_code)