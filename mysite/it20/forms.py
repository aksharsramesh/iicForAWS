from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .import models


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class NEWIdeaSubmissionForm(ModelForm):
    class Meta:
        model = models.newIdea
        fields = ['title', 'contact', 'document']
