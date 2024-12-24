from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Country, League, Team

def Mainpage(request):
    return render(request, 'main_page.html')

def create_records(request):
    if request.method == "POST":

        # Проверяем, есть ли уже созданные данные
        if not Country.objects.filter(title="England").exists():
            # Первая запись
            country1 = Country.objects.create(title="England")
            league1 = League.objects.create(title="Premier League", country=country1)
            Team.objects.create(title="Arsenal", league=league1)

            # Вторая запись
            country2 = Country.objects.create(title="Spain")
            league2 = League.objects.create(title="La Liga", country=country2)
            Team.objects.create(title="Real Madrid", league=league2)

            # Третья запись
            country3 = Country.objects.create(title="Germany")
            league3 = League.objects.create(title="Bundesliga", country=country3)
            Team.objects.create(title="Bayern Munich", league=league3)

            # Четвертая запись
            country4 = Country.objects.create(title="Italy")
            league4 = League.objects.create(title="Serie A", country=country4)
            Team.objects.create(title="Juventus", league=league4)

            # Пятая запись
            country5 = Country.objects.create(title="France")
            league5 = League.objects.create(title="Ligue 1", country=country5)
            Team.objects.create(title="Paris Saint-Germain", league=league5)

            return HttpResponse("5 test records created successfully!")
        else:
            return HttpResponse("Test data already exists!")

    return redirect('main_page')  # Перенаправление на главную страницу, если запрос не POST

