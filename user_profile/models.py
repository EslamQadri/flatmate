from django.db import models
from user_profile.vadiateros import mobile_number_regex
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(User):
    pk = models.UUIDField(primary_key=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    mobile_number = models.CharField(
        "Mobile Number", validators=[mobile_number_regex], max_length=11, unique=True
    )
    is_booked = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
