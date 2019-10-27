from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    login_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ('roll_number', 'login_password', 'name', 'email', 'dept_name', 'cpi', 'batch')
