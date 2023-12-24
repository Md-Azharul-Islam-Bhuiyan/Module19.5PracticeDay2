from django import forms
from musician.models import MusicianModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        

