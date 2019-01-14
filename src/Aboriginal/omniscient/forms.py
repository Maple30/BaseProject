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
        password = forms.CharField(widget=forms.PasswordInput,help_text="帳號或密碼包含不可使用之字元")
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password')

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('Title', 'Context', 'Photo')
# class UserForm(ModelForm):
#     class Meta:
#         password = forms.CharField(widget=forms.PasswordInput)
#         model = User
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
