from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=60)
    info = models.TextField(blank=True)
    
    def __str__(self):
        return self.category_name


class Game(models.Model):
    game_name = models.CharField(max_length=60)
    release_date = models.DateField(null=True)
    game_category = models.ManyToManyField(Category)
    game_info = models.TextField(blank=True)
    game_developers = models.CharField(max_length=60)
    game_publishers = models.CharField(max_length=60)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.game_name

class Company(models.Model):
    company_name = models.CharField(max_length=60)
    info = models.TextField(blank=True)
    date_founded = models.DateField(null=True)
    picture = models.ImageField(null=True, blank=True)
    games = models.ManyToManyField(Game)
    ceo = models.CharField(null=True,max_length=60)


    def __str__(self):
        return self.company_name
