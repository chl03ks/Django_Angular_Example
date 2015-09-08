from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient

from assesment.models import Instructional


class TestAssesmentView(TestCase):

    def setUp(self):
        Instructional.objects.create(title="Example", body="text", source="http://www.google.com")
        self.instruct = Instructional.objects.last()
        user = User(username='admin', is_active=True, is_superuser=True)
        user.set_password('1234')
        user.save()
        self.user = user

    def test_index_view(self):
        self.client.login(username=self.user.username, password="1234")
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_index_api(self):
        self.client.login(username=self.user.username, password="1234")
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

    def test_instructional_view(self):
        self.client.login(username=self.user.username, password="1234")
        response = self.client.get(self.instruct.get_absolute_url())
        self.assertEquals(response.status_code, 200)


class ApiTests(APITestCase):

    def setUp(self):
        Instructional.objects.create(title="Example", body="text", source="http://www.google.com")
        self.instruct = Instructional.objects.last()
        self.api_root = '/api/'
        self.client = APIClient()
        user = User(username='admin', is_active=True, is_superuser=True)
        user.set_password('1234')
        user.save()
        self.user = user

    def test_create_instructional(self):
        """
        Ensure we can get a instructional object.
        """
        self.client.login(username=self.user.username, password="admin")
        response = self.client.get('/api/instructional/1/')
        self.assertEqual(response.data, {"id": 1, "title": "Example", "body": "text", "source": "http://www.google.com", "questions": []})

    def test_create_questions(self):
        """
        Ensure we can get a questions object.
        we didn't add questions to the instructional data so the
        reposnse will be not found
        """
        self.client.login(username=self.user.username, password="admin")
        response = self.client.get('/api/questions/1/')
        self.assertEqual(response.data, {u'detail': u'Not found.'})
