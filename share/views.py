from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Images
from .forms import Verifyform


def home(request):
    return render(request, 'share/home.html')
    # return redirect('accounts/google/login/')


@login_required
def verify(request):
    if request.method == 'GET':
        return render(request, 'share/verify.html', {'form': Verifyform})
    else:
        try:
            form = Verifyform(request.POST)
            form.save()
            # return render(request, 'share/verify.html', {'form': Verifyform})
            return redirect('signin')
        except ValueError:
            return render(request, 'share/verify.html', {'form': Verifyform, 'error': 'Bad Data passed in'})


@login_required
def signin(request):
    images = Images.objects.all()
    return render(request, 'share/signin.html', {'images': images})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        # return redirect('login')
        # return HttpResponse('You have been logged out')
        return redirect('home')

