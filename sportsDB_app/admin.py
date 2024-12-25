from django.contrib import admin
from .models import Country, League, Team
# Register your models here.
# admin.site.register(Country)
# admin.site.register(League)
# admin.site.register(Team)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Отображение имени
    search_fields = ('title',)  # Поиск по имени (в виде списка)

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('title',  'country')  # Исправьте на правильное имя поля
    list_filter = ('country',)  # Фильтр по стране
    search_fields = ('title',)  # Поиск по имени (в виде списка)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Имя команды и лига
    list_filter = ('league',)  # Фильтр по лиге
    search_fields = ('title',)  # Поиск по имени (в виде списка)
