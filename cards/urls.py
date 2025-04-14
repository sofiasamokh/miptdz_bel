"""URL-маршруты для раздела карточек (cards)."""

from django.urls import path
from . import views

# Список маршрутов приложения cards
urlpatterns = [
    # Главная страница карточек: выводит список всех карточек
    path('', views.card_list, name='card_list'),

    # Страница добавления новой карточки
    path('add/', views.add_card, name='add_card'),
]
