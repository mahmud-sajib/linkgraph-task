from django.forms import ModelForm
# importing default user registration form
from django.contrib.auth.forms import UserCreationForm
# importing built-in user model
from django.contrib.auth.forms import User
from django import forms
from blog.models import Writer

# Creating custom User registration form utilizing the default one
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserProfileForm(ModelForm):
    class Meta:
        model = Writer
        fields = ['is_editor']
        
