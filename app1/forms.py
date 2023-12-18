from django.forms import *
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            ]