from django.shortcuts import render, redirect
from scholarships.froms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Scholarships


# Create your views here.

def home(request):
    return render(request, 'index.html')


def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('login')

        return render(request, 'register.html', {'form': form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username OR password is incorrect')
        context = {}
        return render(request, 'login.html', {'form': context})


def logoutUser(request):
    logout(request)
    return redirect('login')


def showData(request):
    data = Scholarships.objects.all()
    return render(request, 'scholarships.html', {'data': data})


@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')
