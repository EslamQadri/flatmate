from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_profile.views import (
    UserProfileCreateView,
    UserProfileRetrieveUpdateDestroyView,
)

tokens_urls = [
    path("init/token/", TokenObtainPairView.as_view(), name="init_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
user_urls = [
    path("user", UserProfileCreateView.as_view(), name="user-list-create"),
    path(
        "user/<uuid:id>/",
        UserProfileRetrieveUpdateDestroyView.as_view(),
        name="user-detail",
    ),
]
urlpatterns = [*tokens_urls, *user_urls]
