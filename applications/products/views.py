from django.shortcuts import render

from django.contrib import messages
#import the Posts module
from django.urls import reverse
from .models import Product, Category, Tag
from django.contrib.auth.decorators import login_required
#importing the modified comment form
#from .forms import AddComment, UpdateInsertion
#CREATING CLASS BASED VIEWS TO BE BLE TO GET PAGES THAT CAN LIST, ADD, UPDATE AND DELETE
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#importing the superclass that is used to make login required in class based views
from django.contrib.auth.mixins import LoginRequiredMixin
#this mixin is to ensure that only the author of the post can modify the post
from django.contrib.auth.mixins import UserPassesTestMixin


'''======= HOME PAGE VIEW ========'''
class HomeView(ListView):
    model = Product
    template_name = 'home'

    ordering = ["-date_posted"]
    paginate_by = 12