from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Country, League, Team
import requests


def Mainpage(request):
    return render(request, 'main_page.html')




