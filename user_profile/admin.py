from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    model = UserProfile

    list_display = (
        "id",
        "username",
        "email",
        "mobile_number",
        "date_joined",
        "is_blocked",
        "is_email_verified",
        "is_mobile_verified",
        "date_of_birth",
    )
    search_fields = ("username", "email", "mobile_number")
    list_filter = ("is_blocked", "is_email_verified", "is_mobile_verified")
    ordering = ("-date_joined",)
    readonly_fields = ("date_joined",)

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "full_name",
                    "mobile_number",
                    "image",
                    "date_of_birth",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Status",
            {"fields": ("is_blocked", "is_email_verified", "is_mobile_verified")},
        ),
        (
            "Important dates",
            {"fields": ("last_login", "date_joined")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
