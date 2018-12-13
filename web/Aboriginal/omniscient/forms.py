from django import forms
from .models import Works
from .models import Issue
from django.contrib.auth.models import User

class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ('Title', 'Introduction', 'Contact', 'Photo')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')