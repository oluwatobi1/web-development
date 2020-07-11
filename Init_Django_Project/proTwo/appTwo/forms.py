from django.forms import ModelForm
from appTwo.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", 'email']
