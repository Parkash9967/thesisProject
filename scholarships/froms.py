from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scholarships.models import Contact


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
