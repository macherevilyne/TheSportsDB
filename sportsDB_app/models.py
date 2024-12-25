from django.db import models

# Create your models here.

class Country(models.Model):
    title = models.CharField(max_length=100)
    flag_url = models.URLField(max_length=200, blank=True, null=True)  # URL флага

    def __str__(self):
        return self.title


class League(models.Model):
    id_leagueAPI = models.CharField(max_length=50,blank=True, null=True) # Charfield а не Integer потому что я неуверен какой в API тип + более универсально
    title = models.CharField(max_length=100)
    title_alternate = models.CharField(max_length=100)
    sport_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title} - {self.country}'



class Team(models.Model):
    title = models.CharField(max_length=100)
    # Основная информация о команде
    id_teamAPI = models.CharField(max_length=100, blank=True, null=True)  # ID команды из API
    id_espn = models.CharField(max_length=100, blank=True, null=True)  # ID ESPN
    id_api_football = models.CharField(max_length=100, blank=True, null=True)  # ID API футбола
    loved = models.IntegerField(blank=True, null=True)  # Оценка "любимости"
    title_alternate = models.CharField(max_length=255, blank=True, null=True)  # Альтернативное название команды
    team_short = models.CharField(max_length=10, blank=True, null=True)  # Сокращенное название команды
    formed_year = models.IntegerField(blank=True, null=True)  # Год основания команды    sport_name = models.ForeignKey(Sport, on_delete=models.CASCADE)
    sport_name = models.CharField(max_length=50)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # # Лига, в которой играет команда
    league = models.ManyToManyField('League', related_name='teams')

    # Дивизион
    division = models.CharField(max_length=100, blank=True,null=True)  # Дивизион (например, "Premier League", "Championship" и т.д.)
    # Стадион
    id_venue = models.CharField(max_length=100, blank=True, null=True)  # ID стадиона
    stadium = models.CharField(max_length=255, blank=True, null=True)  # Название стадиона
    location = models.CharField(max_length=255, blank=True, null=True)  # Местоположение команды
    stadium_capacity = models.IntegerField(blank=True, null=True)  # Вместимость стадиона

    # Контакты
    website = models.URLField(blank=True, null=True)  # Официальный сайт
    facebook = models.URLField(blank=True, null=True)  # Facebook
    twitter = models.URLField(blank=True, null=True)  # Twitter
    instagram = models.URLField(blank=True, null=True)  # Instagram
    rss = models.URLField(blank=True, null=True)  # RSS-канал

    # Описание
    description_en = models.TextField(blank=True, null=True)  # Описание на английском
    description_it = models.TextField(blank=True, null=True)  # Описание на итальянском
    descriptionDE = models.TextField(blank=True, null=True)
    descriptionFR = models.TextField(blank=True, null=True)
    descriptionCN = models.TextField(blank=True, null=True)
    descriptionJP = models.TextField(blank=True, null=True)
    descriptionRU = models.TextField(blank=True, null=True)
    descriptionES = models.TextField(blank=True, null=True)
    descriptionPT = models.TextField(blank=True, null=True)
    descriptionSE = models.TextField(blank=True, null=True)
    descriptionNL = models.TextField(blank=True, null=True)
    descriptionHU = models.TextField(blank=True, null=True)
    descriptionNO = models.TextField(blank=True, null=True)
    descriptionIL = models.TextField(blank=True, null=True)
    descriptionPL = models.TextField(blank=True, null=True)


    # Цвета команды
    colour1 = models.CharField(max_length=7, blank=True, null=True)  # Основной цвет

    # Логотипы и изображения
    badge = models.URLField(blank=True, null=True)  # Логотип
    logo = models.URLField(blank=True, null=True)  # Логотип
    fanart1 = models.URLField(blank=True, null=True)  # Изображение фанарт 1
    banner = models.URLField(blank=True, null=True)  # Баннера
    equipment = models.URLField(blank=True, null=True)  # Оборудование (например, мяч)
    youtube = models.URLField(blank=True, null=True)  # Канал YouTube

    # Статус
    str_locked = models.CharField(max_length=10, blank=True, null=True)  # Статус (заблокирован/разблокирован)

    def __str__(self):
        return f'{self.title} - {self.league}'


