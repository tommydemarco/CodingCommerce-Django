from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequired

# Create your views here.


'''=========> USER PROFILE VIEW '''
class UserProfileView(LoginRequired, TemplateView):
    template_name = 'accounts/profile.html'