from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "student.html", {"talabalar": students})

class LandingView(View):
    def get(self, request):
        return render(request, "index.html")


class UserRegisterView(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_2"]
        if password_1 == password_2:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password_1)
            user.save()
            return redirect("landing")
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "auth/login.html", {"form": form})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.filter(username=username, password=password)
        if user:
            print("<<<<<<<<<<<<<Successfully login>>>>>>>>>>>>>>>>>>>>>")
            return redirect("landing")

        else:
            print("<<<<<<<<<<<<<Fail login>>>>>>>>>>>>>>>>>>>>>")
            return render(request, "user_not_found.html")