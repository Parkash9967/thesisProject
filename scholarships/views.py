from django.shortcuts import render, redirect
from scholarships.froms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Scholarships
from django.core.paginator import Paginator


def home(request):
    return render(request, 'index.html')


def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('index')
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
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'username OR password is incorrect')
        context = {}
        return render(request, 'login.html', {'form': context})


def logoutUser(request):
    logout(request)
    return redirect('home')


def showData(request):
    data = Scholarships.objects.all()
    p = Paginator(data, 15)
    page_number = request.GET.get('page', 1)
    obj = p.get_page(page_number)
    return render(request, 'scholarships.html', {'data': obj})


@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')