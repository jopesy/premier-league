from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("admin/", admin.site.urls),
    path("v1/", include("premier.api.urls")),
]
