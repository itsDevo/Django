from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("games/", views.games),
    path("companies/", views.companies),
    path("categories/", views.categories),
    path("games/<int:pk>", views.one_game),
    path("companies/<int:pk>", views.one_company),
    path("categories/<int:pk>", views.one_category)
]