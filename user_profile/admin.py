from django.contrib import admin
from user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "mobile_number",
        "date_joined",
        "is_booked",
        "is_email_verified",
        "is_mobile_verified",
        "date_of_birth",
    )
    search_fields = ("username", "email", "mobile_number")
    list_filter = ("is_booked", "is_email_verified", "is_mobile_verified")
    ordering = ("-date_joined",)
