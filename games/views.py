from django.shortcuts import render
from .models import Game, Category, Company
# Create your views here.
def index(request):
    content = {
        'games' : Game.objects.all(),
        'companies' : Company.objects.all()
    }
    return render(request,("main/index.html"),content)

def games(request):
    content = {
        'games': Game.objects.all()
    }
    return render(request, 'main/games.html', content)

def one_game(request, pk):
    content = {
        "game" : Game.objects.get(pk=pk)
    }
    return render(request, 'main/one_game.html',content)

def companies(request):
    content = {
        'companies': Company.objects.all()
    }
    return render(request, 'main/companies.html', content)

def one_company(request,pk):
    content = {
        'company': Company.objects.get(pk=pk)
    }
    return render(request, 'main/one_company.html', content)

def categories(request):
    content = {
        'categories': Category.objects.all()
    }
    return render(request, 'main/categories.html', content)

def one_category(request,pk):
    content = {
        'category': Category.objects.get(pk=pk)
    }
    return render(request, 'main/one_category.html', content)