from django.core import management
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from social.models import UserProfile
from social.api.serializer import UserProfileSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        management.call_command('populate_db')


class GetAllUserProfilesTest(BaseViewTest):
    def test_get_all_users(self):
        response = self.client.get(
            reverse("social-api:users-all")
        )
        expected = UserProfile.objects.all()
        serialized = UserProfileSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
