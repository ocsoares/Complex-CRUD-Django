from django.urls import path

from user.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("user/", UserListCreateView.as_view(), name="user_create"),
    path(
        "user/<str:id>",
        UserRetrieveUpdateDestroyView.as_view(),
        name="user_retrieve_update_and_destroy",
    ),
]
