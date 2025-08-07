from django.test import TestCase
from user_profile.models import UserProfile
from datetime import date


class UserProfileModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_profile_creation(self):
        user = UserProfile.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
            mobile_number="1234567890",
            date_of_birth=date(2000, 1, 1),
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.get_full_name, "Test User")
        self.assertEqual(user.mobile_number, "1234567890")
        self.assertEqual(user.date_of_birth.strftime("%Y-%m-%d"), "2000-01-01")
        self.assertFalse(user.is_blocked)
        self.assertFalse(user.is_email_verified)
        self.assertFalse(user.is_mobile_verified)
        self.assertIsNotNone(user.id)
