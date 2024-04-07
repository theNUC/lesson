from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogOutView


urlpatterns = [
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/logout/", UserLogOutView.as_view(), name="logout")
]