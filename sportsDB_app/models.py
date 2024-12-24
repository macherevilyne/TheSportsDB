from django.db import models

# Create your models here.

class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class League(models.Model):
    title = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.country}'

class Team(models.Model):
    title = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title} - {self.league}'