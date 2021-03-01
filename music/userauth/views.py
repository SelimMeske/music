from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from user_profile.models import UserProfile


# Create your views here.
def signup_view(request):


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile(user_name=user.username, description='Hello there, this is the description of yours.', user_fk=user)
            userprofile.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'user_auth/custom_signup.html')


def login_view(request):


    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')

    return render(request, 'user_auth/custom_login.html')


def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('login')