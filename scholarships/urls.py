from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('list/', views.list, name='scholarships'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('top10/', views.top10, name='top10'),
    path('bachelor/', views.bachelor, name='bachelor'),
    path('master/', views.master, name='master'),
    path('phd/', views.phd, name='phd'),
    path('services/', views.services, name='services'),
    path('countries/', views.countries, name='countries'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy')
]
