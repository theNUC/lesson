from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "email", "username", "password")
#
#     def save(self, commit=True):
#         user = super().save(commit)
#         user.set_password(self.cleaned_data["password"])
#         user.save()
#         return user
#
# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ("username", "password")