from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CreateChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = '__all__'

class CreateMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'