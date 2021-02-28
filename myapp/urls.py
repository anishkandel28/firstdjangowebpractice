from django.contrib import admin
from django.urls import path
from myapp import views

# url dispatching
urlpatterns = [
    # path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("service", views.service, name='contact'), 
    path("about/", views.about, name='contact'),
    path("base", views.base, name='base'),
    path("dashboard", views.dashboard, name='base'),

]
