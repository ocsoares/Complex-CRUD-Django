from typing import Any, cast

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: Any):
        user = cast(User, user)

        token = super().get_token(user)
        token["email"] = user.email  # Add field to Token payload
        token["name"] = user.name  # Add field to Token payload
        return token
