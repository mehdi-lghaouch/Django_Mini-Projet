from django import forms
from django.contrib.auth.models import User
from MiniApp.models import UserProfileInfo , Employee

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class EmployeeForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = "__all__"
