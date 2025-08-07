from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_profile.views import (
    UserProfileRetrieveUpdateDestroyView,
    RegisterUserView,
)

tokens_urls = [
    path("init/token/", TokenObtainPairView.as_view(), name="init_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
user_urls = [
    path("create-user", RegisterUserView.as_view(), name="create-user"),
    path(
        "user/<uuid:id>/",
        UserProfileRetrieveUpdateDestroyView.as_view(),
        name="get-update-delete-user",
    ),
]
urlpatterns = [*tokens_urls, *user_urls]
