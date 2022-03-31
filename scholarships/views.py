from django.shortcuts import render, redirect
from scholarships.froms import CreateUserForm, CreateContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Scholarships
from .models import Top10, Contact
from django.core.paginator import Paginator


def index(request):
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
    return redirect('index')


@login_required(login_url='login')
def list(request):
    data = Scholarships.objects.all()
    p = Paginator(data, 5)
    page_number = request.GET.get('page', 1)
    obj = p.get_page(page_number)
    return render(request, 'scholarships.html', {'data': obj})


@login_required(login_url='login')
def home(request):
    query = Scholarships.objects.filter(scholarship_program__icontains='Bachelors')[:3]
    query2 = Scholarships.objects.filter(scholarship_program__icontains='Masters')[:3]
    query3 = Scholarships.objects.filter(scholarship_program__icontains='PhD')[:3]
    return render(request, 'home.html', {'data': query, 'data2': query2, 'data3': query3})


@login_required(login_url='login')
def search(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            scholarships = Scholarships.objects.filter(scholarship_name__icontains=searched)
            return render(request, 'search.html', {'data': scholarships})
        else:
            print("No Scholarship found")
            return render(request, 'search.html', {})


@login_required(login_url='login')
def top10(request):
    data_top = Top10.objects.all()
    return render(request, 'top10.html', {'data': data_top})


@login_required(login_url='login')
def services(request):
    return render(request, 'services.html')


@login_required(login_url='login')
def bachelor(request):
    query = Scholarships.objects.filter(scholarship_program__icontains='Bachelors').all()
    p = Paginator(query, 5)
    page_number = request.GET.get('page', 1)
    obj = p.get_page(page_number)
    return render(request, 'bachelor.html', {'data': obj})


@login_required(login_url='login')
def master(request):
    query2 = Scholarships.objects.filter(scholarship_program__icontains='Masters Degree').all()
    p = Paginator(query2, 5)
    page_number = request.GET.get('page', 1)
    obj = p.get_page(page_number)
    return render(request, 'master.html', {'data': obj})


@login_required(login_url='login')
def phd(request):
    query3 = Scholarships.objects.filter(scholarship_program__icontains='PhD Degree').all()
    p = Paginator(query3, 5)
    page_number = request.GET.get('page', 1)
    obj = p.get_page(page_number)
    return render(request, 'phd.html', {'data': obj})


@login_required(login_url='login')
def countries(request):
    country = request.POST.get('country')
    countries = Scholarships.objects.filter(scholarship_country=country).all()
    return render(request, 'countries.html', {'data': countries})


@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def contact(request):
    form = CreateContactForm()
    if request.method == 'POST':
        instance = Contact()
        instance.full_name = request.POST.get('full_name')
        instance.email = request.POST.get('email')
        instance.message = request.POST.get('message')
        instance.save()
        return redirect('contact')

    return render(request, 'contactUs.html', {'form': form})


@login_required(login_url='login')
def privacy(request):
    return render(request, 'privacy.html')
