from django.test import TestCase
from django.urls import reverse
from user_profile.views import (
    UserProfileRetrieveUpdateDestroyView,
    RegisterUserView,
)
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from user_profile.models import UserProfile
from datetime import date


class UserProfileViewTests(APITestCase):
    def setUp(self):
        self.create_url = reverse("create-user")

        self.valid_payload = {
            "username": "eslam",
            "email": "eslam@example.com",
            "password": "strongpassword123",
            "first_name": "Eslam",
            "last_name": "Qadri",
            "mobile_number": "01012345678",
            "date_of_birth": "2000-01-01",
        }

    def test_create_user_success(self):
        response = self.client.post(self.create_url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(UserProfile.objects.filter(username="eslam").exists())

    def test_create_user_missing_fields(self):
        incomplete_data = self.valid_payload.copy()
        incomplete_data.pop("username")
        response = self.client.post(self.create_url, incomplete_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_returns_tokens(self):
        response = self.client.post(self.create_url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
