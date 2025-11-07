from typing import Any
from uuid import UUID

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from user.models import User
from user.serializers import UserSerializer


# Route /user with GET & POST methods
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("created_at")
    serializer_class = UserSerializer

    def get_permissions(self) -> list[Any]:
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]


# Route /user/<id> with GET, PUT, PATCH and DELETE methods
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by("created_at")
    serializer_class = UserSerializer
    lookup_field = "id"

    # Default ID message error
    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field)

        try:
            formated_uuid = UUID(str(lookup_value))
            return self.queryset.get(id=formated_uuid)
        except (ValueError, User.DoesNotExist) as err:
            raise NotFound(detail="User not found") from err
