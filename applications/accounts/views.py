from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequired
from django.shortcuts import redirect
#login required decorator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserProfileUpdateForm, UserUpdateForm

# Create your views here.


'''=========> USER PROFILE VIEW '''
@login_required 
def profile(request): 
    if request.method == 'POST':
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        u_form = UserUpdateForm(request.POST, instance=request.user) 
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, "Your profile has been updated")
            return redirect('user_profile')
    else:
        p_form = UserProfileUpdateForm(instance=request.user.userprofile)
        u_form = UserUpdateForm(instance=request.user) 
    

    context = {
        'p_form': p_form, 
        'u_form': u_form,
    }

    return render(request, 'accounts/profile.html', context)