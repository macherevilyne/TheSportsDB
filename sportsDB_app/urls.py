from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Mainpage, name='main_page'),
    path('create_records/', views.create_records, name='create_records'),

]