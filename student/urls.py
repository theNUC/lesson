from django.urls import path
from .views import StudentListView, LandingView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path("", LandingView.as_view(), name="landing"),
]