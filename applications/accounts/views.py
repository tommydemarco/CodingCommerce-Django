from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequired
from django.shortcuts import redirect
#login required decorator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserProfileUpdateForm, UserUpdateForm

#importing models
from applications.products.models import Product

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
    s
    context = {
        'p_form': p_form, 
        'u_form': u_form,
    }

    return render(request, 'admin/profile.html', context)

#product list Class based View
class ProductsList(ListView): 
    model: Product
    template_name = 'products_list.html'

    def get_queryset(self):
        return Product.objects.all()
    
