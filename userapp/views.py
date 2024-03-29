from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import random

def register(request):
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            # form.instance.username = f'{random.randrange(10000000)}'
            form.instance.username = form.instance.phone
            form.save()
            phone =form.cleaned_data.get('phone')      
            messages.success(request,f'Account created for {phone}! You are now able to login')
            return redirect('/')
    else:
        form =RegisterForm()
    return render(request, 'userapp/register.html',{'form':form})




@login_required
def profile(request):
    return render(request, 'userapp/profile.html')

@login_required
def profileupdate(request):

    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-update')

    else:
        u_form =  UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {

        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'userapp/profileupdate.html', context)





