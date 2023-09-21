from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from .models import PerevalAdded


class SubmitDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_pereval(self):
        data = {
            "author": {
                "email": "test@example.com",
                "last_name": "Тестов",
                "first_name": "Тест",
                "middle_name": "Тестович",
                "phone": "1234567890"
            },
            "category": {
                "winter": "",
                "spring": "",
                "summer": "",
                "autumn": ""
            },
            "images": {
                "data": "1650892132_13-vsegda-pomnim-com-p-dolina-v-gorakh-foto-17.jpg",
                "title": "123"
            },
            "coords": {
                "latitude": 23,
                "longitude": 23,
                "height": 23
            },
            "beauty_title": "Poss",
            "title": "title",
            "other_titles": "title",
            "area": "planet_earth",
            "type_activity": "walking",
            "connect": "connect",
            "status": "new"
        }

        response = self.client.post("/SubmitData/", data, format="json")
        self.assertTrue(response.status_code in [status.HTTP_201_CREATED, status.HTTP_200_OK])

        self.assertTrue(PerevalAdded.objects.filter(title="title").exists())
