from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase


class PollsAPITestCase(APITestCase):
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_django_celery_results_bug(self):
        data = {"name": "Joe Bloggs"}
        response = self.client.post("/polls/", data)
        assert response.status_code == status.HTTP_201_CREATED
