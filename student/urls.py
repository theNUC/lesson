from django.urls import path
from .views import StudentListView, LandingView, UserRegisterView, UserLoginView

urlpatterns = [
    path("student/", StudentListView.as_view(), name="student"),
    path("", LandingView.as_view(), name="landing"),
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
]