from rest_framework import generics
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated


class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "id"
