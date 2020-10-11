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

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        m, t = avatar.content_type.split('/')

        if not(m == 'image' and (t == 'jpg' or t == 'png')):
            raise forms.ValidationError('You can\'t upload this type of files')

        return avatar 