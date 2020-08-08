from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib import messages

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form =ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated succesfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form =ProfileUpdateForm(instance=request.user.profile)
       
        
    context = {
        'u_form':u_form,
        'p_form':p_form
        
    }
    return render(request, 'users/profile.html', context)