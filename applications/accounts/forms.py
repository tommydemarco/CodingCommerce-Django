from django import forms 
from .models import UserProfile 
from django.contrib.auth.models import User
#from django.core.exeptions import ValidationError 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone']

