from django.contrib import admin
from django.urls import path, include
from .view import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page),
    path("", include("student.urls")),
    path("", include("library.urls")),
]
