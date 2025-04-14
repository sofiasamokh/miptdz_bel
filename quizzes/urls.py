"""Маршруты для раздела "Викторина."""

from django.urls import path
from . import views

urlpatterns = [
    #Страница запуска викторины
    path('start/', views.start_quiz, name='start_quiz'),
    # Если понадобится добавление вопросов вручную через форму — можно раскомментировать:
    # path('add/', views.add_question, name='add_question'),
]