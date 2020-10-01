from django.shortcuts import render

from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
#importing the superclass that is used to make login required in class based views
from django.contrib.auth.mixins import LoginRequiredMixin
#this mixin is to ensure that only the author of the post can modify the post
from django.contrib.auth.mixins import UserPassesTestMixin
#rest framework views
from rest_framework.generics import ListAPIView


'''======= HOME PAGE VIEW ========'''
class HomeView(TemplateView):
    template_name = 'products/home.html'

