from django.db import models
from user_profile.validators import mobile_number_regex
from django.contrib.auth.models import AbstractUser
import uuid


class UserProfile(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField("Username", max_length=150, unique=True, db_index=True)
    email = models.EmailField("Email", unique=True, db_index=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField("First Name", max_length=30, blank=True)
    last_name = models.CharField("Last Name", max_length=30, blank=True)
    full_name = models.CharField("Full Name", max_length=60, blank=True)

    image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    mobile_number = models.CharField(
        "Mobile Number", validators=[mobile_number_regex], max_length=11, unique=True
    )
    is_blocked = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.full_name = self.get_full_name
        super().save(*args, **kwargs)
