from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import ProfileForm
from account.models import Profile


def sign_up_account(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('blog:index')
            except InterruptedError:
                return render(request, 'register.html', {
                    'form': ProfileForm,
                    'error': 'Username already exist. Try another username'
                })
    else:
        return render(request, 'register.html', {
            'form': ProfileForm
        })


def login_account(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password do not exist'
            })
        else:
            login(request, user)
            return redirect('blog:index')
    else:
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })


@login_required
def log_out_account(request):
    logout(request)
    return redirect('blog:index')


@login_required
def profile(request):
    if request.method == 'POST':
        current_profile = get_object_or_404(Profile, user_id=request.user.id)
        profile_form = ProfileForm(request.POST, instance=current_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('blog:index')
    else:
        current_profile = get_object_or_404(Profile, user_id=request.user.id)
        return render(request, 'profile.html', {
            'profile_form': ProfileForm(instance=current_profile)
        })
