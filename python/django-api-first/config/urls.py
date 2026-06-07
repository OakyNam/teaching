from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("frontend_site.urls")),
    path("api/", include("backend_api.urls")),
]
