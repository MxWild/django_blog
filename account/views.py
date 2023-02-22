from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def sign_up_account(request):
    pass


def login_account(request):
    pass


@login_required
def log_out_account(request):
    logout(request)
    return redirect('blog:index')


def profile(request):
    pass
