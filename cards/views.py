"""Представления (views) для работы с карточками: список и форма добавления."""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Card
from .forms import CardForm

def card_list(request):
    #Представление для отображения всех карточек.
    #Карточки сортируются по дате создания (новые сверху).
    cards = Card.objects.all().order_by('-created_at')  # Получаем все карточки из базы
    return render(request, 'cards/card_list.html', {'cards': cards})


def add_card(request):
    """Представление для добавления новой карточки через форму.
    #Поддерживает загрузку изображений и валидацию формы."""
    if request.method == 'POST':
        # Обработка формы с данными и загруженными файлами
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохраняем карточку в базу
            messages.success(request, "Карточка успешно добавлена!")  # Показываем уведомление
            return redirect('card_list')  # Редирект обратно на список карточек
    else:
        form = CardForm()  # Пустая форма для GET-запроса

    return render(request, 'cards/add_card.html', {'form': form})  # Отображение формы
