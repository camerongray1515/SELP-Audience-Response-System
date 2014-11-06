from django.test import TestCase, Client

class TestCourseSelection(TestCase):
    fixtures = ['basic_setup.json']
    
    def makeNewClient(self):
        # Remove any existing clients, make a new one and then login
        self.client = None
        self.client = Client()
        self.client.post('/login/', {'username': 'tutor1', 'password': '1234'})

    # "Select a course" message should be displayed on the tutor page
    def test_no_course_selected(self):
        self.makeNewClient()
        response = self.client.get('/tutor/')
        
        self.assertContains(response, 'you must select a course')
