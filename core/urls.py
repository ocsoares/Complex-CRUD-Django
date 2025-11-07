from django.urls import include, path

urlpatterns = [
    path("api/", include("user.urls")),
    path("api/", include("api.auth.urls")),
]
