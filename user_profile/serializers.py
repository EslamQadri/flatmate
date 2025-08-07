from rest_framework.serializers import ModelSerializer
from user_profile.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
