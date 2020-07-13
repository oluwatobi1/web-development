from django import forms
from .models import People, Student

class Form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = People
        fields = '__all__'
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
