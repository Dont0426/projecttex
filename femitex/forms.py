from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Post   
   
   
mychoices = [('I', 'Imran'), ('KB', 'KB'), ('Alex', 'Alex')]  
class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        models = User()
        fields = ['username', 'email', 'password1', 'password2']
class MyTestForm(forms.Form):
        name = forms.CharField(required=True, label='First Name')
        email = forms.EmailField()
        random = forms.CharField(widget= forms.Textarea())
    
class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)